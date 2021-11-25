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
    def do_convolution(self, output_squares, kernel_squares, stride, speed):
        for i in range(len(output_squares)):
            for j in range(len(output_squares[i])):
                if j == 0 and i != 0:
                    self.play(ApplyMethod(kernel_squares.shift, LEFT*0.75*(len(output_squares[i])-1)*stride, DOWN*0.75*stride, run_time=speed))
                elif j != 0 or i != 0:
                    self.play(ApplyMethod(kernel_squares.shift, RIGHT*0.75*stride), run_time=speed)
                self.play(Create(output_squares[i][j]), run_time=speed)

    # creates outer padding 
    def create_padding(self, height, width, input_length, size, start):
        total_squares = []
        total_zeroes = []
        for i in range(input_length+(height*2)):
            current_row = []
            current_zeroes = []
            for j in range(input_length+(width*2)):
                if i == 0 and j == 0:
                    current_row += Square(side_length=size,color=ORANGE).next_to(start).shift(UP*1.125, LEFT*1.875)
                    current_zeroes += Text("0", color=GREY_E).next_to(start).shift(UP*1.125, LEFT*1.8)
                elif j == 0:
                    current_row += Square(side_length=size,color=ORANGE).next_to(total_squares[i-1][0], DOWN)
                    current_zeroes += Text("0", color=GREY_E).next_to(total_zeroes[i-1][0], DOWN*1.52)

                else:
                    if i < height or i >= input_length+height or j < width or j >= input_length+width:
                        current_row += Square(side_length=size,color=ORANGE).next_to(current_row[j-1], RIGHT)
                        current_zeroes += Text("0", color=GREY_E).next_to(current_zeroes[j-1], RIGHT*1.63)

                    else: 
                        current_row += Square(side_length=size).next_to(current_row[j-1], RIGHT).set_opacity(0)
                        current_zeroes += Text("0", color=GREY_E).next_to(current_zeroes[j-1], RIGHT*1.63).set_opacity(0)
            total_squares += [current_row]
            total_zeroes += [current_zeroes]
        return total_squares, total_zeroes

    # creates inner padding
    def create_inner_padding(self, padding, input_squares, size, start):
        total_squares = []
        total_zeroes = []
        for i in range(len(input_squares)+padding):
            current_row = []
            current_zeroes = []
            for j in range(len(input_squares)+padding):
                if i == 0 and j == 0:
                    current_row += Square(side_length=size,color=YELLOW).next_to(start).shift(UP*0.375, LEFT*1.125).set_opacity(0)
                    current_zeroes += Text("0", color=GREY_E).next_to(start).shift(UP*0.375, LEFT*1.05).set_opacity(0)
                elif j == 0:
                    if i % 2 != 0:
                        current_row += Square(side_length=size,color=RED).next_to(total_squares[i-1][0], DOWN)
                        current_zeroes += Text("0", color=GREY_E).next_to(total_zeroes[i-1][0], DOWN*1.52)
                    else:
                        current_row += Square(side_length=size,color=YELLOW).next_to(total_squares[i-1][0], DOWN).set_opacity(0)
                        current_zeroes += Text("0", color=GREY_E).next_to(total_zeroes[i-1][0], DOWN*1.52).set_opacity(0)
                else:
                    if i % 2 != 0 or j % 2 != 0:
                        current_row += Square(side_length=size,color=RED).next_to(current_row[j-1], RIGHT)
                        current_zeroes += Text("0", color=GREY_E).next_to(current_zeroes[j-1], RIGHT*1.63)
                    else: 
                        current_row += Square(side_length=size,color=YELLOW).next_to(current_row[j-1], RIGHT).set_opacity(0)
                        current_zeroes += Text("0", color=GREY_E).next_to(current_zeroes[j-1], RIGHT*1.63).set_opacity(0)
            total_squares += [current_row]
            total_zeroes += [current_zeroes]
        return total_squares, total_zeroes

        return total_squares

    def construct(self):
        # regular convolution labels
        title = Text("No Padding, Non-Unit Strides Convolution")
        input_text = Text("Input: 4 x 4").shift(UP*3.0, LEFT*1.7).scale(0.7)
        padding_text = Text("Padding: 0 x 0", color=ORANGE).next_to(input_text,DOWN*0.35).scale(0.7)
        kernel_text = Text("Kernel: 2 x 2", color=BLUE).next_to(padding_text,DOWN*0.35).scale(0.7)
        stride_text = Text("Stride: 2 x 2", color=PURPLE).next_to(kernel_text,DOWN*0.35).scale(0.7)
        output_text = Text("Output: 2 x 2", color=YELLOW).next_to(stride_text,DOWN*0.35).scale(0.7)

        # regular input, kernel, and output squares
        input_squares = self.create_squares(4, 4, 0.5, 1, WHITE, 3.0, -1.25)
        kernel_squares = self.create_squares(2, 2, 0.7, 0.2, BLUE, 3.0, -1.25)
        output_squares = self.create_squares(2, 2, 0.5, 1, YELLOW, -1.0, 2)

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
        self.do_convolution(output_squares, kernel_squares_group, 2, 1)

        # display output result
        self.play(Write(output_text))
        self.wait()

        #prepare screen for transposed
        self.play(ApplyMethod(label_group.scale, 0.6), ApplyMethod(input_squares_group.scale, 0.6), 
            ApplyMethod(kernel_squares_group.scale, 0.6, {"about_point":np.array([2.4,1.85,1])}), 
            ApplyMethod(output_squares_group.scale, 0.6))
        self.play(ApplyMethod(label_group.shift, LEFT*3.8, UP*0.6), ApplyMethod(input_squares_group.shift, LEFT*7.9, DOWN*1.6), 
            ApplyMethod(kernel_squares_group.shift, LEFT*7.9, DOWN*1.6), ApplyMethod(output_squares_group.shift, LEFT*3.8, DOWN*0.3))

        # transposed convolution labels
        title_trans = Text("No Padding, Non-Unit Strides").shift(RIGHT, UP*0.5)
        title_trans1 = Text("Transposed Convolution").next_to(title_trans, DOWN)
        input_text_trans = Text("Input: 2 x 2", color=YELLOW).shift(UP*3.1, LEFT*1.3).scale(0.7)
        inner_padding_text1 = Text("Stride Padding: Stride - 1", color=RED).next_to(input_text_trans,DOWN*0.35).scale(0.7)
        inner_padding_text2 = Text("Stride Padding: (2 - 1) x (2 - 1)", color=RED).next_to(input_text_trans,DOWN*0.35).scale(0.7)
        inner_padding_text3 = Text("Stride Padding: 1 x 1", color=RED).next_to(input_text_trans,DOWN*0.35).scale(0.7)
        padding_text_trans1 = Text("Padding: 0 x 0", color=ORANGE).next_to(inner_padding_text1,DOWN*0.35).scale(0.7)
        padding_text_trans2 = Text("p' = Kernel - 1", color=ORANGE).next_to(padding_text_trans1,DOWN*0.35).scale(0.7)
        padding_text_trans3 = Text("p' = (2 - 1) x (2 - 1)", color=ORANGE).next_to(padding_text_trans1,DOWN*0.35).scale(0.7)
        padding_text_trans4 = Text("p' = 1 x 1", color=ORANGE).next_to(padding_text_trans1,DOWN*0.35).scale(0.7)
        kernel_text_trans = Text("Kernel: 2 x 2", color=BLUE).next_to(padding_text_trans1,DOWN*0.35).scale(0.7)
        stride_text_trans1 = Text("Stride: 2 x 2", color=PURPLE).next_to(kernel_text_trans,DOWN*0.35).scale(0.7)
        stride_text_trans2 = Text("s'= 1 x 1", color=PURPLE).next_to(stride_text_trans1,DOWN*0.35).scale(0.7)
        output_text_trans = Text("Output: 4 x 4").next_to(stride_text_trans1,DOWN*0.35).scale(0.7)

        # transposed input, kernel, and output squares
        input_squares_trans = self.create_squares(2, 2, 0.5, 1, YELLOW, 1.8, -2.6)
        kernel_squares_trans = self.create_squares(2, 2, 0.7, 0.2, BLUE, 2.94, -1.46)
        output_squares_trans = self.create_squares(4, 4, 0.5, 1, WHITE, -0.8, 2.4)
        inner_padding_squares_trans, inner_padding_zeroes_trans = self.create_inner_padding(1, input_squares_trans, 0.5, input_squares_trans[0][0])
        padding_squares_trans, padding_zeroes_trans = self.create_padding(1, 1, len(input_squares_trans) + 1, 0.5, input_squares_trans[0][0])

        # transposed input, kernel, and output groups
        input_squares_group_trans = VGroup(*input_squares_trans[0], *input_squares_trans[1])
        kernel_squares_group_trans = VGroup(*kernel_squares_trans[0], *kernel_squares_trans[1])
        output_squares_group_trans = VGroup(*output_squares_trans[0], *output_squares_trans[1], *output_squares_trans[2],
            *output_squares_trans[3])
        inner_padding_squares_group_trans = VGroup(*inner_padding_squares_trans[0], *inner_padding_squares_trans[1], 
            *inner_padding_squares_trans[2])
        inner_padding_zeroes_group_trans = VGroup(*inner_padding_zeroes_trans[0], *inner_padding_zeroes_trans[1], 
            *inner_padding_zeroes_trans[2])
        padding_squares_group_trans = VGroup(*padding_squares_trans[0], *padding_squares_trans[1], *padding_squares_trans[2],
            *padding_squares_trans[3], *padding_squares_trans[4])
        padding_zeroes_group_trans = VGroup(*padding_zeroes_trans[0], *padding_zeroes_trans[1], *padding_zeroes_trans[2],
            *padding_zeroes_trans[3], *padding_zeroes_trans[4])
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
        self.play(Create(inner_padding_squares_group_trans), Create(inner_padding_zeroes_group_trans))
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
        self.play(Create(padding_squares_group_trans), Create(padding_zeroes_group_trans))
        self.play(FadeOut(padding_text_trans2))

        # display kernel
        self.play(Write(kernel_text_trans))
        self.play(Create(kernel_squares_group_trans))

        # display and do strides
        self.play(Write(stride_text_trans1))
        self.play(Write(stride_text_trans2))
        self.wait(0.5) 
        self.play(FadeOut(stride_text_trans2))
        self.do_convolution(output_squares_trans, kernel_squares_group_trans, 1, 0.5)

        # display output result
        self.play(Write(output_text_trans))
        self.wait(3)