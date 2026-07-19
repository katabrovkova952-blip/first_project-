import math
import random


SIZE = 4
DIRECTIONS = ("up", "down", "left", "right")
SPAWN = ((2, 0.9), (4, 0.1))
WIN_TILE = 2048
LOSS_PENALTY = -1_000_000

# ─────────────────────────── ЛОГІКА ХОДІВ ───────────────────────────

def _merge_left(row):
    """Стискає й зливає один рядок вліво. Повертає (новий_рядок, бали).
    Правило балів: a+a -> 2a дає +2a; кілька злиттів за хід — додаються."""
    tiles = [v for v in row if v != 0]
    result, gained, i = [], 0, 0
    while i < len(tiles):
        if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
            merged = tiles[i] * 2
            result.append(merged)
            gained += merged
            i += 2
        else:
            result.append(tiles[i])
            i += 1
    result += [0] * (SIZE - len(result))
    return result, gained


def _transpose(board):
    return [list(row) for row in zip(*board)]


def apply_move(board, direction):
    """Хід у напрямку, не псуючи вхідну дошку.
    Повертає (нова_дошка, бали, чи_зрушилось)."""
    gained = 0
    if direction == "left":
        new = []
        for row in board:
            r, g = _merge_left(row); new.append(r); gained += g
    elif direction == "right":
        new = []
        for row in board:
            r, g = _merge_left(row[::-1]); new.append(r[::-1]); gained += g
    elif direction == "up":
        cols = []
        for col in _transpose(board):
            r, g = _merge_left(col); cols.append(r); gained += g
        new = _transpose(cols)
    elif direction == "down":
        cols = []
        for col in _transpose(board):
            r, g = _merge_left(col[::-1]); cols.append(r[::-1]); gained += g
        new = _transpose(cols)
    else:
        raise ValueError(direction)
    return new, gained, (new != board)


def empties(board):
    return [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]


def with_tile(board, r, c, value):
    """КОПІЯ дошки з поставленою плиткою. Глибока копія рядків (row[:]) —
    інакше мутація однієї гілки зіпсує сусідні через спільні посилання."""
    nb = [row[:] for row in board]
    nb[r][c] = value
    return nb


def won(board):
    return any(v >= WIN_TILE for row in board for v in row)


def has_moves(board):
    if empties(board):
        return True
    return any(apply_move(board, d)[2] for d in DIRECTIONS)


# ─────────────────────────── ОЦІНКА ПОЗИЦІЇ ───────────────────────────

def _log2(v):
    return math.log2(v) if v > 0 else 0.0


def _mono_line(line):
    vals = [_log2(v) for v in line]
    inc = dec = 0.0
    for a, b in zip(vals, vals[1:]):
        if b > a: inc += (b - a)
        elif a > b: dec += (a - b)
    return -min(inc, dec)


def _monotonicity(board):
    total = 0.0
    for row in board:
        total += _mono_line(row)
    for col in _transpose(board):
        total += _mono_line(col)
    return total


def _smoothness(board):
    total = 0.0
    for r in range(SIZE):
        for c in range(SIZE):
            v = board[r][c]
            if v == 0: continue
            lv = _log2(v)
            if c + 1 < SIZE and board[r][c + 1]:
                total -= abs(lv - _log2(board[r][c + 1]))
            if r + 1 < SIZE and board[r + 1][c]:
                total -= abs(lv - _log2(board[r + 1][c]))
    return total


def _corner_bonus(board):
    """Найбільшу плитку тримаємо в кутку — так надійно виростають 1024,
    а нам їх треба ДВІ, щоб мати чим склеїти 2048 в останній момент."""
    m = max(max(r) for r in board)
    corners = (board[0][0], board[0][SIZE-1], board[SIZE-1][0], board[SIZE-1][SIZE-1])
    return 2.0 * _log2(m) if m in corners else 0.0


def evaluate(board):
    """Позиційний бонус у листку дерева (НЕ бали — бали накопичуються окремо
    по дорозі). Оцінює здоров'я позиції: чи виживемо й чи зможемо будувати далі.
      • порожні клітинки — простір для маневру (виживання);
      • монотонність + кут — структура, у якій ростуть великі плитки;
      • гладкість — близькі сусіди легше злити."""
    empty = len(empties(board))
    return (3.5 * empty
            + 1.0 * _monotonicity(board)
            + 0.1 * _smoothness(board)
            + _corner_bonus(board))


# ─────────────────────────── ЕКСПЕКТИМАКС + ВІДКЛАДАННЯ 2048 ─────────────────
#
# Ключова зміна проти старої версії: хід, що робить 2048, ми НЕ розглядаємо,
# поки є хоч один інший безпечний хід і на полі ще є місце. 2048 "заряджаємо"
# лише коли поле майже повне (cash_in) або коли інших ходів просто нема (forced).
# Без цього пошук з коротким горизонтом хапає 2048 одразу (бо +2048 — найбільший
# разовий приз) і завершує гру рано з малим рахунком.


def _adaptive_depth(n_empty, base):
    if n_empty >= 8: return base
    if n_empty >= 4: return base + 1
    if n_empty >= 2: return base + 2
    return base + 3


def _candidate_moves(board, hold_2048, cash_in):
    """Які ходи взагалі дозволені зараз (з урахуванням відкладання 2048).
    Повертає список (напрямок, нова_дошка, бали, це_перемога)."""
    legal = []
    for d in DIRECTIONS:
        nb, g, moved = apply_move(board, d)
        if moved:
            legal.append((d, nb, g, won(nb)))
    if not hold_2048:
        return legal

    safe = [m for m in legal if not m[3]]          # ходи, що НЕ роблять 2048
    win_moves = [m for m in legal if m[3]]
    n_empty = len(empties(board))

    if win_moves and n_empty <= cash_in:
        return win_moves                            # поле повне -> час забирати перемогу
    if safe:
        return safe                                 # ще є куди рости -> відкладаємо 2048
    return legal                                    # безвиході -> 2048 вимушено


def _move_node(board, depth, cache, hold_2048, cash_in):
    key = (_key(board), depth)
    if key in cache:
        return cache[key]
    if depth == 0:
        v = evaluate(board); cache[key] = v; return v

    best = None
    for d, nb, gained, is_win in _candidate_moves(board, hold_2048, cash_in):
        if is_win:
            val = gained                            # перемога: гра стоп, майбутнього нема
        else:
            val = gained + _chance_node(nb, depth, cache, hold_2048, cash_in)
        if best is None or val > best:
            best = val
    if best is None:
        best = LOSS_PENALTY
    cache[key] = best
    return best


def _chance_node(board, depth, cache, hold_2048, cash_in):
    cells = empties(board)
    if not cells:
        return _move_node(board, depth - 1, cache, hold_2048, cash_in)
    p_cell = 1.0 / len(cells)
    total = 0.0
    for (r, c) in cells:
        for value, prob in SPAWN:
            nb = with_tile(board, r, c, value)
            total += p_cell * prob * _move_node(nb, depth - 1, cache, hold_2048, cash_in)
    return total


def _key(board):
    return tuple(tuple(row) for row in board)


def best_move(board, base_depth=3, hold_2048=True, cash_in=1):
    """Порадник. Повертає (напрямок, очікувана_цінність, оцінки_всіх_ходів).
      hold_2048=True  -> відкладати 2048, набивати поле (максимум балів);
      hold_2048=False -> грати 2048 звичайно (просто перемогти швидше);
      cash_in         -> при скількох порожніх клітинках уже "забирати" 2048."""
    depth = _adaptive_depth(len(empties(board)), base_depth)
    cache = {}
    allowed = _candidate_moves(board, hold_2048, cash_in)
    allowed_dirs = {m[0] for m in allowed}

    scores = {d: None for d in DIRECTIONS}
    for d, nb, gained, is_win in allowed:
        if is_win:
            scores[d] = gained
        else:
            scores[d] = gained + _chance_node(nb, depth, cache, hold_2048, cash_in)

    playable = [d for d in DIRECTIONS if scores[d] is not None]
    best = max(playable, key=lambda d: scores[d]) if playable else None
    return best, (scores[best] if best else None), scores


# ─────────────────────────── САМА ГРА ───────────────────────────

class Game2048:
    def __init__(self):
        self.board = [[0] * SIZE for _ in range(SIZE)]
        self.score = 0
        self._spawn(); self._spawn()

    def _spawn(self):
        cells = empties(self.board)
        if not cells: return
        r, c = random.choice(cells)
        self.board[r][c] = 2 if random.random() < 0.9 else 4

    def move(self, direction):
        nb, gained, moved = apply_move(self.board, direction)
        if not moved:
            return False
        self.board = nb
        self.score += gained
        if not won(self.board):        # після перемоги нову плитку не ставимо — гра стоп
            self._spawn()
        return True

    def won(self):
        return won(self.board)

    def over(self):
        return self.won() or not has_moves(self.board)

    def show(self):
        print(f"Бали: {self.score}")
        for row in self.board:
            print(" ".join(f"{v:5d}" if v else "    ." for v in row))
        print()


# ─────────────────────────── ЗРУЧНІ ОБГОРТКИ ───────────────────────────

_NAMES = {"up": "ВГОРУ", "down": "ВНИЗ", "left": "ВЛІВО", "right": "ВПРАВО"}


def recommend(board, base_depth=3, hold_2048=True, cash_in=1):
    best, _, scores = best_move(board, base_depth, hold_2048, cash_in)
    print("Оцінки ходів (більше = краще; None = зараз недоступний/відкладений):")
    for d in DIRECTIONS:
        s = scores[d]
        print(f"  {_NAMES[d]:6} — {'—' if s is None else f'{s:9.1f}'}")
    print(f"\n>>> Найкращий хід: {_NAMES[best]}\n" if best else "\nХодів немає.\n")
    return best


def autoplay(base_depth=2, hold_2048=True, cash_in=1, max_moves=None, show_every=0):
    game = Game2048()
    moves = 0
    while not game.over() and (max_moves is None or moves < max_moves):
        d, _, _ = best_move(game.board, base_depth, hold_2048, cash_in)
        if d is None:
            break
        game.move(d)
        moves += 1
        if show_every and moves % show_every == 0:
            game.show()
    game.show()
    biggest = max(max(r) for r in game.board)
    status = "ПЕРЕМОГА (2048)" if game.won() else ("глухий кут" if game.over() else "ліміт ходів")
    print(f"[{status}] ходів: {moves} | бали: {game.score} | найбільша: {biggest}")
    return game


if __name__ == "__main__":
    sample = [
        [2, 2, 16, 16],
        [32, 8, 64, 4],
        [8, 512, 2, 1024],
        [0, 4, 512, 2],
    ]
    recommend(sample, base_depth=3)
    # autoplay(base_depth=2)          # max_moves за замовчуванням None -> без ліміту