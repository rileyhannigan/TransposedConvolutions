from manim import *
import numpy as np

class PaddingUnitStrides(Scene):
    
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
    def do_convolution(self, output_squares, kernel_squares):
        for i in range(len(output_squares)):
            for j in range(len(output_squares[i])):
                if j == 0 and i != 0:
                    self.play(ApplyMethod(kernel_squares.shift, LEFT*0.75*(len(output_squares[i])-1), DOWN*0.75))
                elif j != 0 or i != 0:
                    self.play(ApplyMethod(kernel_squares.shift, RIGHT*0.75))
                self.play(Create(output_squares[i][j]))

   # creates padding 
    def create_padding(self, height, width, input_squares, size, start):
        total_squares = []
        for i in range(len(input_squares)+(height*2)):
            current_row = []
            for j in range(len(input_squares[0])+(width*2)):
                if i == 0 and j == 0:
                    current_row += Square(side_length=size,color=ORANGE).next_to(start).shift(UP*0.75, LEFT*1.5)
                elif j == 0:
                    current_row += Square(side_length=size,color=ORANGE).next_to(total_squares[i-1][0], DOWN)
                else:
                    if i < height or i >= len(input_squares)+height or j < width or j >= len(input_squares[0])+width:
                        current_row += Square(side_length=size,color=ORANGE).next_to(current_row[j-1], RIGHT)
                    else: 
                        current_row += Square(side_length=size).next_to(current_row[j-1], RIGHT).set_opacity(0)
            total_squares += [current_row]
        return total_squares
   
    def construct(self):
        # regular convolution labels
        title = Text("Padding, Unit Strides Convolution")
        input_text = Text("Input: 3 x 4").shift(UP*3.0, LEFT*1.7).scale(0.7)
        padding_text = Text("Padding: 1 x 1", color=ORANGE).next_to(input_text,DOWN*0.35).scale(0.7)
        kernel_text = Text("Kernel: 2 x 2", color=BLUE).next_to(padding_text,DOWN*0.35).scale(0.7)
        stride_text = Text("Stride: 1 x 1").next_to(kernel_text,DOWN*0.35).scale(0.7)
        output_text = Text("Output: 4 x 5", color=PURPLE).next_to(stride_text,DOWN*0.35).scale(0.7)

        # regular input, kernel, and output squares
        input_squares = self.create_squares(3, 4, 0.5, 1, WHITE, 2.0, -1.75)
        kernel_squares = self.create_squares(2, 2, 0.7, 0.2, BLUE, 2.75, -1)
        output_squares = self.create_squares(4, 5, 0.5, 1, PURPLE, -0.5, 3.3)
        padding_squares = self.create_padding(1, 1, input_squares, 0.5, input_squares[0][0])

        # regular input, kernel, output, and label groups
        input_squares_group = VGroup(*input_squares[0], *input_squares[1], *input_squares[2])
        kernel_squares_group = VGroup(*kernel_squares[0], *kernel_squares[1])
        output_squares_group = VGroup(*output_squares[0], *output_squares[1], *output_squares[2], *output_squares[3])
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
        self.do_convolution(output_squares, kernel_squares_group)

        # display output result
        self.play(Write(output_text))
        self.wait()

        #prepare screen for transposed
        self.play(ApplyMethod(label_group.scale, 0.6), ApplyMethod(input_squares_group.scale, 0.6), 
            ApplyMethod(kernel_squares_group.scale, 0.6, {"about_point":np.array([2.86,1.27,1])}), 
            ApplyMethod(output_squares_group.scale, 0.6), ApplyMethod(padding_squares_group.scale, 0.6))
        self.play(ApplyMethod(label_group.shift, LEFT*3.4, UP*0.7), ApplyMethod(input_squares_group.shift, LEFT*8, DOWN*0.9), 
            ApplyMethod(kernel_squares_group.shift, LEFT*8, DOWN*0.9), ApplyMethod(output_squares_group.shift, LEFT*3.3, DOWN*0.3),
            ApplyMethod(padding_squares_group.shift, LEFT*8, DOWN*0.9))

        # # transposed convolution labels
        # title_trans = Text("No Padding, Unit Strides").shift(RIGHT, UP*0.5)
        # title_trans1 = Text("Transposed Convolution").next_to(title_trans, DOWN)
        # input_text_trans = Text("Input: 3 x 3", color=PURPLE).shift(UP*3.1, LEFT*1.3).scale(0.7)
        # padding_text_trans_1 = Text("Padding: 0 x 0", color=ORANGE).next_to(input_text_trans,DOWN*0.35).scale(0.7)
        # padding_text_trans_2 = Text("p' = Kernel - 1", color=ORANGE).next_to(padding_text_trans_1,DOWN*0.35).scale(0.7)
        # padding_text_trans_3 = Text("p' = 3 - 1 x 3 - 1", color=ORANGE).next_to(padding_text_trans_1,DOWN*0.35).scale(0.7)
        # padding_text_trans_4 = Text("p' = 2 x 2", color=ORANGE).next_to(padding_text_trans_1,DOWN*0.35).scale(0.7)
        # kernel_text_trans = Text("Kernel: 3 x 3", color=BLUE).next_to(padding_text_trans_1,DOWN*0.35).scale(0.7)
        # stride_text_trans = Text("Stride: 1 x 1").next_to(kernel_text_trans,DOWN*0.35).scale(0.7)
        # output_text_trans = Text("Output: 5 x 5").next_to(stride_text_trans,DOWN*0.35).scale(0.7)

        # # transposed input, kernel, and output squares
        # input_squares_trans = self.create_squares(3, 3, 0.5, 1, PURPLE, 3, -3)
        # kernel_squares_trans = self.create_squares(3, 3, 0.7, 0.2, BLUE, 3, -1.5)
        # output_squares_trans = self.create_squares(5, 5, 0.5, 1, WHITE, 0, 2.7)
        # padding_squares_trans = self.create_padding(2, 2, input_squares_trans, 0.5)

        # # transposed input, kernel, and output groups
        # input_squares_group_trans = VGroup(*input_squares_trans[0], *input_squares_trans[1], *input_squares_trans[2])
        # kernel_squares_group_trans = VGroup(*kernel_squares_trans[0], *kernel_squares_trans[1], *kernel_squares_trans[2])
        # output_squares_group_trans = VGroup(*output_squares_trans[0], *output_squares_trans[1], *output_squares_trans[2],
        #     *output_squares_trans[3], *output_squares_trans[4])
        # padding_squares_group_trans = VGroup(*padding_squares_trans[0], *padding_squares_trans[1], *padding_squares_trans[2],
        #     *padding_squares_trans[3], *padding_squares_trans[4], *padding_squares_trans[5], *padding_squares_trans[6])

        # #display title
        # self.play(Write(title_trans), Write(title_trans1))
        # self.wait()
        # self.play(FadeOut(title_trans), FadeOut(title_trans1))

        # # display input
        # self.play(Write(input_text_trans)) 
        # self.play(Create(input_squares_group_trans))

        # # display padding
        # self.play(Write(padding_text_trans_1)) 
        # self.wait(0.5)
        # self.play(Write(padding_text_trans_2))
        # self.wait(0.5) 
        # self.play(Transform(padding_text_trans_2, padding_text_trans_3)) 
        # self.wait(0.5)
        # self.play(Transform(padding_text_trans_2, padding_text_trans_4)) 
        # self.wait(0.5)
        # self.play(ApplyMethod(input_squares_group_trans.shift, DOWN*0.75*2))
        # self.play(Create(padding_squares_group_trans))
        # self.play(FadeOut(padding_text_trans_2))

        # # display kernel
        # self.play(Write(kernel_text_trans))
        # self.play(Create(kernel_squares_group_trans))

        # # display and do strides
        # self.play(Write(stride_text_trans))
        # self.do_convolution(output_squares_trans, kernel_squares_group_trans)

        # # display output result
        # self.play(Write(output_text_trans))
        # self.wait(3)