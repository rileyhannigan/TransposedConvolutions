from manim import *
import numpy as np

class PaddingNonUnitStrides(Scene):
    
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
    def create_padding(self, height, width, input_height, input_width, size, start):
        total_squares = []
        for i in range(input_height+(height*2)):
            current_row = []
            for j in range(input_width+(width*2)):
                if i == 0 and j == 0:
                    current_row += Square(side_length=size,color=ORANGE).next_to(start).shift(UP*0.75, LEFT*1.5)
                elif j == 0:
                    current_row += Square(side_length=size,color=ORANGE).next_to(total_squares[i-1][0], DOWN)
                else:
                    if i < height or i >= input_height+height or j < width or j >= input_width+width:
                        current_row += Square(side_length=size,color=ORANGE).next_to(current_row[j-1], RIGHT)
                    else: 
                        current_row += Square(side_length=size).next_to(current_row[j-1], RIGHT).set_opacity(0)
            total_squares += [current_row]
        return total_squares

    # creates inner padding
    def create_inner_padding(self, padding, input_squares, size, start):
        total_squares = []
        for i in range(len(input_squares)+padding):
            current_row = []
            for j in range(len(input_squares)+padding):
                if i == 0 and j == 0:
                    current_row += Square(side_length=size,color=PURPLE).next_to(start).shift(UP*0.375, LEFT*1.125).set_opacity(0)
                elif j == 0:
                    if i % 2 != 0:
                        current_row += Square(side_length=size,color=RED).next_to(total_squares[i-1][0], DOWN)
                    else:
                        current_row += Square(side_length=size,color=PURPLE).next_to(total_squares[i-1][0], DOWN).set_opacity(0)
                else:
                    if i % 2 != 0 or j % 2 != 0:
                        current_row += Square(side_length=size,color=RED).next_to(current_row[j-1], RIGHT)
                    else: 
                        current_row += Square(side_length=size,color=PURPLE).next_to(current_row[j-1], RIGHT).set_opacity(0)
            total_squares += [current_row]
        return total_squares
   
    def construct(self):
        # regular convolution labels
        title = Text("Padding, Non-Unit Strides Convolution")
        input_text = Text("Input: 3 x 4").shift(UP*3.0, LEFT*1.7).scale(0.7)
        padding_text = Text("Padding: 1 x 1", color=ORANGE).next_to(input_text,DOWN*0.35).scale(0.7)
        kernel_text = Text("Kernel: 3 x 3", color=BLUE).next_to(padding_text,DOWN*0.35).scale(0.7)
        stride_text = Text("Stride: 2 x 2").next_to(kernel_text,DOWN*0.35).scale(0.7)
        output_text = Text("Output: 2 x 2", color=PURPLE).next_to(stride_text,DOWN*0.35).scale(0.7)

        # regular input, kernel, and output squares
        input_squares = self.create_squares(3, 4, 0.5, 1, WHITE, 2.0, -1.75)
        kernel_squares = self.create_squares(3, 3, 0.7, 0.2, BLUE, 2.75, -1)
        output_squares = self.create_squares(2, 2, 0.5, 1, PURPLE, -0.5, 2.1)
        padding_squares = self.create_padding(1, 1, len(input_squares), len(input_squares[0]), 0.5, input_squares[0][0])

        # regular input, kernel, output, and label groups
        input_squares_group = VGroup(*input_squares[0], *input_squares[1], *input_squares[2])
        kernel_squares_group = VGroup(*kernel_squares[0], *kernel_squares[1], *kernel_squares[2])
        output_squares_group = VGroup(*output_squares[0], *output_squares[1])
        label_group = Group(input_text, padding_text, kernel_text, stride_text, output_text)
        padding_squares_group = VGroup(*padding_squares[0], *padding_squares[1], *padding_squares[2],
            *padding_squares[3], *padding_squares[4])

        #display title
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        # display input
        self.play(Write(input_text)) 
        self.play(Create(input_squares_group))

        # display padding (none)
        self.play(Write(padding_text)) 
        self.play(Create(padding_squares_group))
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
            ApplyMethod(kernel_squares_group.scale, 0.6, {"about_point":np.array([2.86,1.27,1])}), 
            ApplyMethod(output_squares_group.scale, 0.6), ApplyMethod(padding_squares_group.scale, 0.6))
        self.play(ApplyMethod(label_group.shift, LEFT*3.4, UP*0.7), ApplyMethod(input_squares_group.shift, LEFT*8, DOWN*0.9), 
            ApplyMethod(kernel_squares_group.shift, LEFT*8, DOWN*0.9), ApplyMethod(output_squares_group.shift, LEFT*3.4, DOWN*0.7),
            ApplyMethod(padding_squares_group.shift, LEFT*8, DOWN*0.9))

        # transposed convolution labels
        title_trans = Text("Padding, Non-Unit Strides").shift(RIGHT, UP*0.5)
        title_trans1 = Text("Transposed Convolution").next_to(title_trans, DOWN)
        input_text_trans = Text("Input: 2 x 2", color=PURPLE).shift(UP*3.1, LEFT*1.3).scale(0.7)
        inner_padding_text1 = Text("Inner Padding: Stride - 1", color=RED).next_to(input_text_trans,DOWN*0.35).scale(0.7)
        inner_padding_text2 = Text("Inner Padding: 2 - 1 x 2 - 1", color=RED).next_to(input_text_trans,DOWN*0.35).scale(0.7)
        inner_padding_text3 = Text("Inner Padding: 1 x 1", color=RED).next_to(input_text_trans,DOWN*0.35).scale(0.7)
        padding_text_trans1 = Text("Padding: 1 x 1", color=ORANGE).next_to(inner_padding_text1,DOWN*0.35).scale(0.7)
        padding_text_trans2 = Text("p' = Kernel - 1", color=ORANGE).next_to(padding_text_trans1,DOWN*0.35).scale(0.7)
        padding_text_trans3 = Text("p' = 3 - 1 x 3 - 1", color=ORANGE).next_to(padding_text_trans1,DOWN*0.35).scale(0.7)
        padding_text_trans4 = Text("p' = 1 x 1", color=ORANGE).next_to(padding_text_trans1,DOWN*0.35).scale(0.7)
        kernel_text_trans = Text("Kernel: 3 x 3", color=BLUE).next_to(padding_text_trans1,DOWN*0.35).scale(0.7)
        stride_text_trans1 = Text("Stride: 2 x 2").next_to(kernel_text_trans,DOWN*0.35).scale(0.7)
        stride_text_trans2 = Text("s'= 1 x 1").next_to(stride_text_trans1,DOWN*0.35).scale(0.7)
        output_text_trans = Text("Output: 3 x 4").next_to(stride_text_trans1,DOWN*0.35).scale(0.7)

        # transposed input, kernel, and output squares
        input_squares_trans = self.create_squares(2, 2, 0.5, 1, PURPLE, 1.8, -2.6)
        kernel_squares_trans = self.create_squares(3, 3, 0.7, 0.2, BLUE, 2.94, -1.46)
        output_squares_trans = self.create_squares(3, 4, 0.5, 1, WHITE, -1, 2.7)
        inner_padding_squares_trans = self.create_inner_padding(1, input_squares_trans, 0.5, input_squares_trans[0][0])
        padding_squares_trans = self.create_padding(1, 1, len(input_squares_trans)+1, len(input_squares_trans[0])+1, 0.5, 
            input_squares_trans[0][0].shift(UP*0.375, LEFT*0.375))

        input_squares_trans[0][0].shift(DOWN*0.375, RIGHT*0.375)

        # transposed input, kernel, and output groups
        input_squares_group_trans = VGroup(*input_squares_trans[0], *input_squares_trans[1])
        kernel_squares_group_trans = VGroup(*kernel_squares_trans[0], *kernel_squares_trans[1], *kernel_squares_trans[2])
        output_squares_group_trans = VGroup(*output_squares_trans[0], *output_squares_trans[1], *output_squares_trans[2])
        inner_padding_squares_group_trans = VGroup(*inner_padding_squares_trans[0], *inner_padding_squares_trans[1], 
            *inner_padding_squares_trans[2])
        padding_squares_group_trans = VGroup(*padding_squares_trans[0], *padding_squares_trans[1], *padding_squares_trans[2],
            *padding_squares_trans[3], *padding_squares_trans[4])

        #display title
        self.play(Write(title_trans), Write(title_trans1))
        self.wait()
        self.play(FadeOut(title_trans), FadeOut(title_trans1))

        # display input
        self.play(Write(input_text_trans)) 
        self.play(Create(input_squares_group_trans))

        # display inner padding
        self.play(Write(inner_padding_text1)) 
        self.wait(0.5) 
        self.play(Transform(inner_padding_text1, inner_padding_text2)) 
        self.wait(0.5)
        self.play(Transform(inner_padding_text1, inner_padding_text3)) 
        self.wait(0.5)
        self.play(ApplyMethod(input_squares_trans[0][0].shift, UP*0.375, LEFT*0.375), ApplyMethod(input_squares_trans[0][1].shift, UP*0.375, RIGHT*0.375),
            ApplyMethod(input_squares_trans[1][0].shift, DOWN*0.375, LEFT*0.375), ApplyMethod(input_squares_trans[1][1].shift, DOWN*0.375, RIGHT*0.375))
        self.play(Create(inner_padding_squares_group_trans))
        self.wait()

        # display padding
        self.play(Write(padding_text_trans1)) 
        self.wait(0.5)
        self.play(Write(padding_text_trans2))
        self.wait(0.5) 
        self.play(Transform(padding_text_trans2, padding_text_trans3)) 
        self.wait(0.5)
        self.play(Transform(padding_text_trans2, padding_text_trans4)) 
        self.wait(0.5)
        self.play(Create(padding_squares_group_trans))
        self.play(FadeOut(padding_text_trans2))

        # display kernel
        self.play(Write(kernel_text_trans))
        self.play(Create(kernel_squares_group_trans))

        # display and do strides
        self.play(Write(stride_text_trans1))
        self.play(Write(stride_text_trans2))
        self.wait(0.5) 
        self.play(FadeOut(stride_text_trans2))
        self.do_convolution(output_squares_trans, kernel_squares_group_trans, 1)

        # display output result
        self.play(Write(output_text_trans))
        self.wait(3)