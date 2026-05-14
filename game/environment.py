import tkinter as tk

class App(tk.Tk):
    def __init__(self, player):
        super().__init__()

        self.canvas = tk.Canvas(self, width=500, height=500,
                                borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.rows = 20
        self.columns = 20
        self.cell_width = 25
        self.cell_height = 25
        self.player = player

        self.rect = {}
        self.oval = {}

        # currently selected circle
        self.selected = None

        for column in range(self.columns):
            for row in range(self.rows):

                x1 = column * self.cell_width
                y1 = row * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height

                # background rectangle
                self.rect[row, column] = self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill="whitesmoke",
                    outline="gray"
                )

                # circle
                oval = self.canvas.create_oval(
                    x1 + 2, y1 + 2,
                    x2 - 2, y2 - 2,
                    fill="white",
                    tags="oval"
                )

                self.oval[row, column] = oval

                # bind click event
                self.canvas.tag_bind(
                    oval,
                    "<Button-1>",
                    lambda event, r=row, c=column: self.select_circle(r, c)
                )

    def update_position(self, character=None, color=None):
        if character is None:
            character = self.player
            # fill new selected circle
        self.canvas.itemconfig(
            self.oval[character["position"][0], character["position"][1]],
            fill="dodgerblue" if color is None else color
        )

    # def select_circle(self, row, column):
    #
    #     # remove previous selection
    #     if self.selected is not None:
    #         old_row, old_col = self.selected
    #         self.canvas.itemconfig(
    #             self.oval[old_row, old_col],
    #             fill="white"
    #         )
    #
    #     # fill new selected circle
    #     self.canvas.itemconfig(
    #         self.oval[row, column],
    #         fill="dodgerblue"
    #     )
    #
    #     # store selection
    #     self.selected = (row, column)
    #

if __name__ == "__main__":
    app = App()
    app.mainloop()

