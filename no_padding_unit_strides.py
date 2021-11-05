from manim import *

class NoPaddingUnitStrides(Scene):
    
    # creates lists of lists of squares, used for input, kernel, and output
    def create_squares(self, height, width, size, padding, c, up_shift, left_shift):
        total_squares = []
        for i in range(height):
            current_row = []
            for j in range(width):
                if i == 0 and j == 0:
                    current_row += Square(side_length=size,color=c).shift(UP*up_shift, LEFT*left_shift)
                elif j == 0:
                    current_row += Square(side_length=size,color=c).next_to(total_squares[i-1][0], DOWN*padding)
                else:
                    current_row += Square(side_length=size,color=c).next_to(current_row[j-1], RIGHT*padding)
            total_squares += [current_row]
        return total_squares

    # moves kernel around and displays output squares one at a time
    def do_convolution(self, output_squares, kernel_squares_group):
        for i in range(len(output_squares)):
            for j in range(len(output_squares[i])):
                if j == 0 and i != 0:
                    self.play(ApplyMethod(kernel_squares_group.shift, LEFT*1.5, DOWN*0.75))
                elif j != 0 or i != 0:
                    self.play(ApplyMethod(kernel_squares_group.shift, RIGHT*0.75))
                self.play(Create(output_squares[i][j]))
   
    def construct(self):
        # regular convolution labels
        input_text = Text("Input: 5x5").shift(UP*3, RIGHT*3)
        padding_text = Text("Padding: 0x0").next_to(input_text,DOWN)
        kernel_text = Text("Kernel: 3x3").next_to(padding_text,DOWN)
        stride_text = Text("Stride: 1x1").next_to(kernel_text,DOWN)
        output_text = Text("Output: 3x3").next_to(stride_text,DOWN)

        # regular input, kernel, and output squares
        input_squares = self.create_squares(5, 5, 0.5, 1, WHITE, 3.5, 6.5)
        kernel_squares = self.create_squares(3, 3, 0.7, 0.2, BLUE, 3.5, 6.5)
        output_squares = self.create_squares(3, 3, 0.5, 1, PURPLE, -0.5, 4)

        # input, kernel, and output groups
        input_squares_group = VGroup(*input_squares[0], *input_squares[1], *input_squares[2],
            *input_squares[3], *input_squares[4])
        kernel_squares_group = VGroup(*kernel_squares[0], *kernel_squares[1], *kernel_squares[2])
        output_squares_group = VGroup(*output_squares[0], *output_squares[1], *output_squares[2])

        # display input
        self.play(Write(input_text)) 
        self.play(Create(input_squares_group))

        # display padding (none)
        self.play(Write(padding_text)) 
        self.wait()

        # display kernel
        self.play(Write(kernel_text))
        self.play(Create(kernel_squares_group))

        # display and do strides
        self.play(Write(stride_text))
        self.do_convolution(output_squares, kernel_squares_group)

        # display output result
        self.play(Write(output_text))