import neopixel


class NeoPixMatrix:
    BLUE = (0, 0, 255)
    CLEAR = (0, 0, 0)
    CYAN = (0, 255, 255)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    def __init__(self, neo_pixels, n_rows, n_cols):
        """Initialize the NeoPixMatrix.

        Args:
            neo_pixels (neopixel.NeoPixel): The NeoPixel matrix.
            n_rows (int): The number of rows in the matrix.
            n_cols (int): The number of columns in the matrix.

        Returns:
            None
        """
        # Check the construction arguments
        assert isinstance(neo_pixels, neopixel.NeoPixel), "No NeoPixel matrix passed."
        assert 0 < n_rows <= 100, f"Illegal n_rows: {n_rows}."
        assert 0 < n_cols <= 100, f"Illegal n_cols: {n_cols}."
        assert n_rows * n_cols == neo_pixels.n, "N rows/cols does not match matrix."
        # Set our attributes.
        self.pix = neo_pixels
        self.n_rows = n_rows
        self.n_cols = n_cols

    def _row_col_to_n(self, row, col):
        """Convert row and column to a single index.

        Args:
            row (int): The row index.
            col (int): The column index.

        Returns:
            int: The single index corresponding to the row and column.
        """
        return row * self.n_cols + col

    def set_pix(self, row, col, color=CLEAR, show=False):
        """Set the color of a specific pixel.

        Args:
            row (int): The row index of the pixel.
            col (int): The column index of the pixel.
            color (tuple, optional): The color to set the pixel to. Defaults to (0, 0, 0).
            show (bool, optional): Whether to update the display immediately. Defaults to False.

        Returns:
            None
        """
        self.pix[self._row_col_to_n(row, col)] = color
        if show:
            self.pix.write()

    def set_row(self, row, color=(0, 0, 0), show=False):
        """Set the color of an entire row.

        Args:
            row (int): The row index.
            color (tuple, optional): The color to set the row to. Defaults to (0, 0, 0).
            show (bool, optional): Whether to update the display immediately. Defaults to False.

        Returns:
            None
        """
        for c in range(self.n_cols):
            self.set_pix(row, c, color)
        if show:
            self.pix.write()

    def set_col(self, col, color=(0, 0, 0), show=False):
        """Set the color of an entire column.

        Args:
            col (int): The column index.
            color (tuple, optional): The color to set the column to. Defaults to (0, 0, 0).
            show (bool, optional): Whether to update the display immediately. Defaults to False.

        Returns:
            None
        """
        for r in range(self.n_rows):
            self.set_pix(r, col, color)
        if show:
            self.pix.write()

    def clear(self, show=True):
        """Clear the entire matrix by setting all pixels to the clear color.

        Args:
            show (bool, optional): Whether to update the display immediately. Defaults to True.

        Returns:
            None
        """
        self.pix.fill(self.CLEAR)
        if show:
            self.pix.write()
