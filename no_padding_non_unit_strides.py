from manim import *
import numpy as np

class NoPaddingNonUnitStrides(Scene):
    
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
    def do_convolution(self, output_squares, kernel_squares, stride):
        for i in range(len(output_squares)):
            for j in range(len(output_squares[i])):
                if j == 0 and i != 0:
                    self.play(ApplyMethod(kernel_squares.shift, LEFT*0.75*(len(output_squares[i])-1)*stride, DOWN*0.75*stride))
                elif j != 0 or i != 0:
                    self.play(ApplyMethod(kernel_squares.shift, RIGHT*0.75*stride))
                self.play(Create(output_squares[i][j]))

    # creates padding 
    def create_padding(self, height, width, input_squares, size, padding):
        total_squares = []
        for i in range(len(input_squares)+(height*2)):
            current_row = []
            for j in range(len(input_squares)+(width*2)):
                if i == 0 and j == 0:
                    current_row += Square(side_length=size,color=ORANGE).shift(UP*3.0, LEFT*-1.5)
                elif j == 0:
                    if i < height or i >= len(input_squares)+height or j < width or j >= len(input_squares)+width:
                        current_row += Square(side_length=size,color=ORANGE).next_to(total_squares[i-1][0], DOWN*padding)
                    else:
                        current_row += Square(side_length=size).next_to(total_squares[i-1][0], DOWN*padding).set_opacity(0)
                else:
                    if i < height or i >= len(input_squares)+height or j < width or j >= len(input_squares)+width:
                        current_row += Square(side_length=size,color=ORANGE).next_to(current_row[j-1], RIGHT*padding)
                    else: 
                        current_row += Square(side_length=size).next_to(current_row[j-1], RIGHT*padding).set_opacity(0)
            total_squares += [current_row]
        return total_squares

    def construct(self):
        # regular convolution labels
        title = Text("No Padding, Non-Unit Strides Convolution")
        input_text = Text("Input: 4 x 4").shift(UP*3.0, LEFT*1.7).scale(0.7)
        padding_text = Text("Padding: 0 x 0", color=ORANGE).next_to(input_text,DOWN*0.35).scale(0.7)
        kernel_text = Text("Kernel: 2 x 2", color=BLUE).next_to(padding_text,DOWN*0.35).scale(0.7)
        stride_text = Text("Stride: 2 x 2").next_to(kernel_text,DOWN*0.35).scale(0.7)
        output_text = Text("Output: 2 x 2", color=PURPLE).next_to(stride_text,DOWN*0.35).scale(0.7)

        # regular input, kernel, and output squares
        input_squares = self.create_squares(4, 4, 0.5, 1, WHITE, 3.0, -1.25)
        kernel_squares = self.create_squares(2, 2, 0.7, 0.2, BLUE, 3.0, -1.25)
        output_squares = self.create_squares(2, 2, 0.5, 1, PURPLE, -1.0, 2)

        # regular input, kernel, output, and label groups
        input_squares_group = VGroup(*input_squares[0], *input_squares[1], 
            *input_squares[2], *input_squares[3])
        kernel_squares_group = VGroup(*kernel_squares[0], *kernel_squares[1])
        output_squares_group = VGroup(*output_squares[0], *output_squares[1])
        label_group = Group(input_text, padding_text, kernel_text, stride_text, output_text)

        #display title
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

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
        self.do_convolution(output_squares, kernel_squares_group, 2)

        # display output result
        self.play(Write(output_text))
        self.wait()

        #prepare screen for transposed
        self.play(ApplyMethod(label_group.scale, 0.6), ApplyMethod(input_squares_group.scale, 0.6), 
            ApplyMethod(kernel_squares_group.scale, 0.6, {"about_point":np.array([2.4,1.85,1])}), 
            ApplyMethod(output_squares_group.scale, 0.6))
        self.play(ApplyMethod(label_group.shift, LEFT*3.8, UP*0.6), ApplyMethod(input_squares_group.shift, LEFT*7.9, DOWN*1.6), 
            ApplyMethod(kernel_squares_group.shift, LEFT*7.9, DOWN*1.6), ApplyMethod(output_squares_group.shift, LEFT*3.8, DOWN*0.3))