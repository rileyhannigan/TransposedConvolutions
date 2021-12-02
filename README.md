# Transposed Convolutions

The following videos demonstrate different cases of regular convolutions and their equivalent transposed convolutions. They can be used as a visual aid when teaching machine learning and were created to be used by the University of Toronto Mississauga's CSC311: Introduction to Machine Learning and CSC413: Neural Networks and Deep Learning classes. 

## No Padding, Unit Strides Convolution

https://user-images.githubusercontent.com/28056407/144500239-5532ea71-c6b9-4d52-b0d8-b2bf86ee8ad7.mp4

This video shows regular and transposed convolutions for the case when there is no padding (0x0) and the stride is 1x1. The input is 5x5 and the kernel is 3x3. First the regular convoltion is setup and the kernel is moved around the input, one stride at a time, creating the 3x3 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, with the kernel moving around and the transposed output being displayed one stride at a time.

## No Padding, Strided Convolution

https://user-images.githubusercontent.com/28056407/144500141-8de05e60-06c9-4e2b-b252-6c0526a68261.mp4

This video shows regular and transposed convolutions for the case when there is no padding and the stride is 2x2. The input is 4x4 and the kernel is 2x2. First the regular convoltion is setup and the kernel is moved around the input, one stride (of two units) at a time, creating the 2x2 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, including the necessary 1x1 stride padding, with the kernel moving around and the transposed output being displayed one stride at a time.

## Padding, Unit Strides Convolution

https://user-images.githubusercontent.com/28056407/144509043-6c15e3ff-6c38-4eed-bf04-1788b655cac6.mp4

This video shows regular and transposed convolutions for the case when there is 1x1 padding and the stride is 1x1. The input is 3x4 and the kernel is 2x2. First the regular convoltion is setup and the kernel is moved around the input, one stride at a time, creating the 4x5 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, with the kernel moving around and the transposed output being displayed one stride at a time.

## Padding, Strided Convolution

https://user-images.githubusercontent.com/28056407/144500218-d03bcb0d-0b83-4a47-a32b-bc8a9d84e3ec.mp4

This video shows regular and transposed convolutions for the case when there is 1x1 padding and the stride is 2x2. The input is 3x4 and the kernel is 3x3. First the regular convoltion is setup and the kernel is moved around the input, one stride (of two units) at a time, creating the 2x2 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, including the necessary 1x1 stride padding and 0x1 additional padding, with the kernel moving around and the transposed output being displayed one stride at a time.

# Installation

To render videos on your local machine Python and manim must be installed.

# Acknowledgements

[A guide to convolution arithmetic for deep learning](https://github.com/vdumoulin/conv_arithmetic) was heavilty referenced when completing these videos.
