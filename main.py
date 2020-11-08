from tkinter import *


class LinkedListVisualisation:
    list_start_point = [200, 300]
    item_size = 50
    distance = 50

    def __init__(self, root):
        self.linkedList = ["foo", "bar", "fubar", "bazl", "bla", "blub", "blob"]
        # self.linkedList = ["foo", "bar", "fubar"]

        canvas_size = (len(self.linkedList)+1)*(self.item_size + self.distance)+2*self.list_start_point[0]

        self.canvas = Canvas(root, width=canvas_size, height=500)
        self.canvas.pack()

    def run(self):
        self.draw_list(self.canvas)
        self.draw_head(self.canvas)

    def draw_list(self, canvas: Canvas):
        x_coord = self.list_start_point[0]
        y_coord = self.list_start_point[1]
        size = self.item_size

        i = 0
        for item in self.linkedList:
            canvas.create_rectangle(x_coord, y_coord, x_coord + size, y_coord + size)
            canvas.create_text(x_coord + size / 2, y_coord + size / 2, text=item)

            if i == 0:
                canvas.create_text(x_coord-self.distance-20, y_coord+size/2+10, text="None")
            else:
                canvas.create_line(x_coord-self.distance, y_coord+size/2-10, x_coord, y_coord+size/2-10, arrow=LAST)

            # last item
            if i == len(self.linkedList)-1:
                canvas.create_line(x_coord+size, y_coord+size/2-10, x_coord+size+self.distance, y_coord+size/2-10, arrow=LAST)
                canvas.create_text(x_coord+self.distance+size+20, y_coord+size/2-10, text="None")

            canvas.create_line(x_coord-self.distance, y_coord+size/2+10, x_coord, y_coord+size/2+10, arrow=FIRST)
            x_coord += self.distance+size
            i += 1

    def draw_head(self, canvas):
        distance = self.distance
        x_coord = self.list_start_point[0]+distance
        y_coord = self.list_start_point[1]-4*distance
        size = self.item_size

        head_size = 2*size
        line_height = 30

        canvas.create_rectangle(x_coord, y_coord, x_coord + size, y_coord + head_size)
        canvas.create_text(x_coord+size/2, y_coord+10, text="first")
        canvas.create_text(x_coord+size/2, y_coord+line_height+10, text="last")
        canvas.create_text(x_coord+size/2, y_coord+2*line_height+10, text="count: " + str(len(self.linkedList)))

        canvas.create_line(x_coord,
                           y_coord + 10,
                           self.list_start_point[0] + self.item_size / 2,
                           self.list_start_point[1],
                           arrow=LAST)

        last_element_x_coord = (len(self.linkedList)+1)*(self.item_size + self.distance)
        canvas.create_line(x_coord + size,
                           y_coord + 10 + line_height,
                           last_element_x_coord + self.item_size / 2,
                           self.list_start_point[1],
                           arrow=LAST)


if __name__ == '__main__':
    window = Tk()
    window.title("Linked List Visualizer")

    visualisation = LinkedListVisualisation(window)
    visualisation.run()

    window.mainloop()
