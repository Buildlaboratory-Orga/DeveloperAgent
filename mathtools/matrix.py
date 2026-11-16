"""Basic linear algebra for small square matrices (lists of rows)."""

EPSILON = 1e-12


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    """Return the transposed matrix."""
    return [list(row) for row in zip(*matrix)]


def multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Return the matrix product a * b."""
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("matrix dimensions do not match.")
    columns = transpose(b)
    return [[sum(x * y for x, y in zip(row, column)) for column in columns] for row in a]


def _check_square(matrix: list[list[float]]) -> int:
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be square and not empty.")
    return n


def _pivot_row(rows: list[list[float]], column: int) -> int:
    """Return the index of the row with the largest absolute value in `column`."""
    return max(range(column, len(rows)), key=lambda r: abs(rows[r][column]))


def determinant(matrix: list[list[float]]) -> float:
    """Return the determinant (Gaussian elimination with partial pivoting)."""
    n = _check_square(matrix)
    rows = [list(row) for row in matrix]
    result = 1.0
    for column in range(n):
        pivot = _pivot_row(rows, column)
        if abs(rows[pivot][column]) < EPSILON:
            return 0.0
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
        result *= rows[column][column]
        for r in range(column + 1, n):
            factor = rows[r][column] / rows[column][column]
            for c in range(column, n):
                rows[r][c] -= factor * rows[column][c]
    return result


def solve(matrix: list[list[float]], right_side: list[float]) -> list[float]:
    """Solve the linear system matrix * x = right_side and return x.

    Raises ValueError if the matrix is singular.
    """
    n = _check_square(matrix)
    if len(right_side) != n:
        raise ValueError("right_side must have one value per row.")
    rows = [list(row) for row in matrix]
    values = list(right_side)
    for column in range(n):
        pivot = _pivot_row(rows, column)
        if abs(rows[pivot][column]) < EPSILON:
            raise ValueError("matrix is singular.")
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
        for r in range(column + 1, n):
            factor = rows[r][column] / rows[column][column]
            for c in range(column, n):
                rows[r][c] -= factor * rows[column][c]
            values[r] -= factor * values[column]
    solution = [0.0] * n
    for r in range(n - 1, -1, -1):
        known = sum(rows[r][c] * solution[c] for c in range(r + 1, n))
        solution[r] = (values[r] - known) / rows[r][r]
    return solution
