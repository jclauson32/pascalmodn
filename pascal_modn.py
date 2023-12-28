## AUTHOR: JOSEPH CLAUSON 2023############
##########################################
import tkinter as tk

def create_grid(canvas, size_canvas, step):
    """
    Adds a grid to a tkinter canvas.
    
    Args:
    - canvas (tk.Canvas): The canvas to which the grid will be added.
    - size_canvas (int): The size (width and height) of the canvas.
    - step (int): The distance between the grid lines.
    """
    # Create vertical lines at intervals of 'step' across the canvas
    for i in range(0, size_canvas, step):
        canvas.create_line([(i, 0), (i, size_canvas)])

    # Create horizontal lines at intervals of 'step' down the canvas
    for i in range(0, size_canvas, step):
        canvas.create_line([(0, i), (size_canvas, i)])

class PascalTriangle:
    def __init__(self, nbr_rows, size_canvas=1500, bg_color='white'):
        """
        Initializes an instance of PascalTriangle.

        Args:
        - nbr_rows (int): The number of rows in Pascal's triangle.
        - size_canvas (int, optional): The size of the canvas. Defaults to 1500.
        - bg_color (str, optional): Background color of the canvas. Defaults to 'white'.
        """
        self.z = 0  # Variable used for modulo operations in derived classes
        self.n = 700  # Unused variable
        self.nbr_rows = nbr_rows  # Number of rows in Pascal's triangle
        self.size_canvas = size_canvas  # Size of the canvas
        self.step = int(size_canvas / nbr_rows)  # Step size between elements in a row
        self.root = tk.Tk()  # Create a Tkinter window
        self.root.title(f"Pascal's triangle of size {nbr_rows}")  # Set the window title
        self.canvas = tk.Canvas(self.root, height=size_canvas, width=size_canvas, bg=bg_color)  # Create a canvas
        
        create_grid(self.canvas, size_canvas, self.step)  # Add a grid to the canvas

    def compute_new_row(self, current_row):
        """
        Computes the next row in Pascal's triangle.

        Args:
        - current_row (list[int]): The current row of Pascal's triangle.

        Returns:
        - list[int]: The next row of Pascal's triangle.
        """
        # Generate next row based on the sum of adjacent numbers in the current row
        return [1] + [sum(x) for x in zip(current_row[1:], current_row[:-1])] + [1]

    def fill_row(self, current_row, current_index):
        """
        Fills a row in the canvas with the values from Pascal's triangle.

        Args:
        - current_row (list[int]): The row from Pascal's triangle to display.
        - current_index (int): The index of the row in the canvas.
        """
        # Place each number in the current row at its corresponding position on the canvas
        for col in range(current_index):
            self.canvas.create_text(col * self.step + self.step / 2, 
                                    (current_index - col) * self.step - self.step / 2,
                                    text=str(current_row[col]))

    def build(self):
        """Builds Pascal's triangle on the canvas."""
        current_row = [1]  # Starting with the first row of Pascal's triangle
        for current_index in range(1, self.nbr_rows + 1):
            self.fill_row(current_row, current_index)  # Fill each row on the canvas
            current_row = self.compute_new_row(current_row)  # Compute the next row

    def plot(self):
        """Plots the entire Pascal's triangle."""
        self.build()  # Build the triangle
        self.canvas.pack()  # Pack the canvas into the Tkinter window
        self.root.mainloop()  # Start the Tkinter event loop

class PascalTriangleMod2(PascalTriangle):
    def __init__(self, nbr_rows, size_canvas=1600, bg_color='black'):
        """
        Initializes an instance of PascalTriangleMod2, a variant of PascalTriangle.

        Args:
        - nbr_rows (int): The number of rows in Pascal's triangle.
        - size_canvas (int, optional): The size of the canvas. Defaults to 1600.
        - bg_color (str, optional): Background color of the canvas. Defaults to 'black'.
        """
        super().__init__(nbr_rows, size_canvas, bg_color)  # Initialize the base class
        self.root.title(f"Pascal's triangle modulo n of size {nbr_rows}")  # Set window title
        self.colors = ['yellow'] * 1000  # Array to hold colors for the visual representation
        self.colors[0] = 'black'  # Set the first color to black

    def fill_row(self, current_row, current_index):
        """
        Fills a row in the canvas with colored rectangles based on Pascal's triangle modulo 2.

        Args:
        - current_row (list[int]): The row from Pascal's triangle to display.
        - current_index (int): The index of the row in the canvas.
        """
        # Determine binary values for the current row, modulo 'z'
        if(self.z == 0):
            binary_row = [0]
        else:
            binary_row = [nbr % self.z for nbr in current_row]
        
        self.z += 1  # Increment 'z' for the next iteration

        # Create colored rectangles for each number in the row
        for col in range(current_index):
            self.canvas.create_rectangle((col + 1) * self.step, 
                                         (current_index - col - 1) * self.step, 
                                         col * self.step, (current_index - col) * self.step, 
                                         fill=self.colors[binary_row[col]], outline=self.colors[binary_row[col]])

if __name__ == '__main__':
    p_triangle_mod_2 = PascalTriangleMod2(800, size_canvas=1600)  # Create an instance of PascalTriangleMod2
    p_triangle_mod_2.plot()  # Plot the triangle
