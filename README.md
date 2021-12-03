# Transposed Convolutions

The following videos demonstrate different cases of regular convolutions and their equivalent transposed convolutions. They can be used as a visual aid when teaching machine learning and were created to be used by the University of Toronto Mississauga's CSC311: Introduction to Machine Learning and CSC413: Neural Networks and Deep Learning classes. 

## No Padding, Unit Strides Convolution

https://user-images.githubusercontent.com/28056407/144511559-02e33e1e-d62b-4033-ad42-379f9cd62a3d.mp4

This video shows regular and transposed convolutions for the case when there is no padding (0x0) and the stride is 1x1. The input is 5x5 and the kernel is 3x3. First the regular convoltion is setup and the kernel is moved around the input, one stride at a time, creating the 3x3 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, with the kernel moving around and the transposed output being displayed one stride at a time.

## No Padding, Strided Convolution

https://user-images.githubusercontent.com/28056407/144512003-6d4e351b-f8a9-4b30-a4f4-1e415471e729.mp4

This video shows regular and transposed convolutions for the case when there is no padding and the stride is 2x2. The input is 4x4 and the kernel is 2x2. First the regular convoltion is setup and the kernel is moved around the input, one stride (of two units) at a time, creating the 2x2 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, including the necessary 1x1 stride padding, with the kernel moving around and the transposed output being displayed one stride at a time.

## Padding, Unit Strides Convolution

https://user-images.githubusercontent.com/28056407/144511030-15149988-c2eb-498f-8a42-c7ed2f062b03.mp4

This video shows regular and transposed convolutions for the case when there is 1x1 padding and the stride is 1x1. The input is 3x4 and the kernel is 2x2. First the regular convoltion is setup and the kernel is moved around the input, one stride at a time, creating the 4x5 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, with the kernel moving around and the transposed output being displayed one stride at a time.

## Padding, Strided Convolution

https://user-images.githubusercontent.com/28056407/144512566-4678b403-4a39-48c2-aec9-0260028d7612.mp4

This video shows regular and transposed convolutions for the case when there is 1x1 padding and the stride is 2x2. The input is 3x4 and the kernel is 3x3. First the regular convoltion is setup and the kernel is moved around the input, one stride (of two units) at a time, creating the 2x2 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, including the necessary 1x1 stride padding and 0x1 additional padding, with the kernel moving around and the transposed output being displayed one stride at a time.

# Installation

To render videos on your local machine Python and manim must be installed.

# Acknowledgements

[A guide to convolution arithmetic for deep learning](https://github.com/vdumoulin/conv_arithmetic) was heavily referenced when completing these videos.

The video animations were created using [the community version of Manim](https://github.com/ManimCommunity/manim).
