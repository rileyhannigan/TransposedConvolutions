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
                    self.play(ApplyMethod(kernel_squares_group.shift, LEFT*0.75*(len(output_squares[i])-1), DOWN*0.75))
                elif j != 0 or i != 0:
                    self.play(ApplyMethod(kernel_squares_group.shift, RIGHT*0.75))
                self.play(Create(output_squares[i][j]))

    # creates padding 
    def create_padding(self, height, width, input_squares, size, padding):
        total_squares = []
        for i in range(len(input_squares)+(height*2)):
            current_row = []
            for j in range(len(input_squares)+(width*2)):
                if i == 0 and j == 0:
                    current_row += Square(side_length=size,color=ORANGE).shift(UP*3.5, LEFT*-1.5)
                elif j == 0:
                    if i < height or i >= len(input_squares)+height or j < width or j >= len(input_squares)+width:
                        current_row += Square(side_length=size,color=ORANGE).next_to(total_squares[i-1][0], DOWN*padding)
                    else:
                        current_row += Square(side_length=size, color=WHITE).next_to(total_squares[i-1][0], DOWN*padding)
                else:
                    if i < height or i >= len(input_squares)+height or j < width or j >= len(input_squares)+width:
                        current_row += Square(side_length=size,color=ORANGE).next_to(current_row[j-1], RIGHT*padding)
                    else: 
                        current_row += Square(side_length=size, color=WHITE).next_to(current_row[j-1], RIGHT*padding)
            total_squares += [current_row]
        return total_squares
   
    def construct(self):
        # regular convolution labels
        input_text = Text("Input: 5x5").shift(UP*3.5, LEFT*1.75).scale(0.7)
        padding_text = Text("Padding: 0x0").next_to(input_text,DOWN).scale(0.7)
        kernel_text = Text("Kernel: 3x3").next_to(padding_text,DOWN).scale(0.7)
        stride_text = Text("Stride: 1x1").next_to(kernel_text,DOWN).scale(0.7)
        output_text = Text("Output: 3x3").next_to(stride_text,DOWN).scale(0.7)

        # regular input, kernel, and output squares
        input_squares = self.create_squares(5, 5, 0.5, 1, WHITE, 3.5, 6.7)
        kernel_squares = self.create_squares(3, 3, 0.7, 0.2, BLUE, 3.5, 6.7)
        output_squares = self.create_squares(3, 3, 0.5, 1, PURPLE, -0.5, 4)

        # regular input, kernel, output, and label groups
        input_squares_group = VGroup(*input_squares[0], *input_squares[1], *input_squares[2],
            *input_squares[3], *input_squares[4])
        kernel_squares_group = VGroup(*kernel_squares[0], *kernel_squares[1], *kernel_squares[2])
        output_squares_group = VGroup(*output_squares[0], *output_squares[1], *output_squares[2])
        label_group = Group(input_text, padding_text, kernel_text, stride_text, output_text)

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
        self.wait()

        #prepare screen for transposed
        self.play(ApplyMethod(label_group.scale, 0.6), ApplyMethod(input_squares_group.scale, 0.6), 
            ApplyMethod(kernel_squares_group.scale, 0.6), ApplyMethod(output_squares_group.scale, 0.6))

        self.play(ApplyMethod(label_group.shift, LEFT*4.1, UP*0.8), ApplyMethod(input_squares_group.shift, LEFT*0.7, DOWN*1.8), 
            ApplyMethod(kernel_squares_group.shift, LEFT*1, DOWN*1.5), ApplyMethod(output_squares_group.shift, LEFT*2.7, DOWN))

        # transposed convolution labels
        input_text_trans = Text("Input: 3x3").shift(UP*3.5, LEFT*1.3).scale(0.7)
        padding_text_trans_1 = Text("Padding: Kernel - 1").next_to(input_text_trans,DOWN).scale(0.7)
        padding_text_trans_2 = Text("Padding: 3 - 1 x 3 - 1").next_to(input_text_trans,DOWN).scale(0.7)
        padding_text_trans_3 = Text("Padding: 2x2").next_to(input_text_trans,DOWN).scale(0.7)
        kernel_text_trans = Text("Kernel: 3x3").next_to(padding_text_trans_1,DOWN).scale(0.7)
        stride_text_trans = Text("Stride: 1x1").next_to(kernel_text_trans,DOWN).scale(0.7)
        output_text_trans = Text("Output: 5x5").next_to(stride_text_trans,DOWN).scale(0.7)

        # transposed input, kernel, and output squares
        input_squares_trans = self.create_squares(3, 3, 0.5, 1, WHITE, 3.5, -3)
        kernel_squares_trans = self.create_squares(3, 3, 0.7, 0.2, BLUE, 3.5, -1.5)
        output_squares_trans = self.create_squares(5, 5, 0.5, 1, PURPLE, -0.5, 2.7)
        padding_squares_trans = self.create_padding(2, 2, input_squares_trans, 0.5, 1)

        # transposed input, kernel, and output groups
        input_squares_group_trans = VGroup(*input_squares_trans[0], *input_squares_trans[1], *input_squares_trans[2])

        kernel_squares_group_trans = VGroup(*kernel_squares_trans[0], *kernel_squares_trans[1], *kernel_squares_trans[2])
        output_squares_group_trans = VGroup(*output_squares_trans[0], *output_squares_trans[1], *output_squares_trans[2],
            *output_squares_trans[3], *output_squares_trans[4])
        padding_squares_group_trans = VGroup(*padding_squares_trans[0], *padding_squares_trans[1], *padding_squares_trans[2],
            *padding_squares_trans[3], *padding_squares_trans[4], *padding_squares_trans[5], *padding_squares_trans[6])

        # display input
        self.play(Write(input_text_trans)) 
        self.play(Create(input_squares_group_trans))

        # display padding
        self.play(Write(padding_text_trans_1)) 
        self.wait(0.5)
        self.play(Transform(padding_text_trans_1, padding_text_trans_2)) 
        self.wait(0.5)
        self.play(Transform(padding_text_trans_1, padding_text_trans_3)) 
        self.wait(0.5)
        self.play(ApplyMethod(input_squares_group_trans.shift, DOWN*0.75*2))
        self.play(Create(padding_squares_group_trans))


        # display kernel
        self.play(Write(kernel_text_trans))
        self.play(Create(kernel_squares_group_trans))

        # display and do strides
        self.play(Write(stride_text_trans))
        self.do_convolution(output_squares_trans, kernel_squares_group_trans)

        # display output result
        self.play(Write(output_text_trans))
        self.wait(3)