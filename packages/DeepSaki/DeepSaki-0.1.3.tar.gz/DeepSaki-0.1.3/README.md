# DeepSaki
Welcome AI enthuisiasts to DeepSaki, a collection of reusable machine learning code. :muscle::robot::metal:

The ML framework used is tensorflow and the entire code is suitable to run Google's TPUs.

![GitHub](https://img.shields.io/github/license/sascha-kirch/deepsaki)

# Installation

## Git
```
git clone https://github.com/sascha-kirch/DeepSaki.git
```

## Pip
![PyPI](https://img.shields.io/pypi/v/deepsaki)
![PyPI - Status](https://img.shields.io/pypi/status/deepsaki)
![PyPI - Downloads](https://img.shields.io/pypi/dm/deepsaki?label=downloads%20pip)
```
pip install DeepSaki
```

# Content
- activations
  - ComplexActivation
- initializer
  - HeAlphaNormal
  - HeAlphaUniform
  - helper
    - MakeInitializerComplex
- layers
  - GlobalSumPooling2D
  - ReflectionPadding (suitable for TPU)
  - FourierConvolution2D
  - rFFTPooling2D
  - FourierFilter2D
  - FourierPooling2D
  - FFT2D
  - iFFT2D
  - Conv2DBlock
  - Conv2DSplitted
  - DenseBlock
  - DownSampleBlock
  - UpSampleBlock
  - ResidualIdentityBlock
  - ResBlockDown
  - ResBlockUp
  - ScaleLayer
  - ScalarGatedSelfAttention
  - Encoder
  - Bottleneck
  - Decoder
  - helper
    - GetInitializer
    - pad_func
    - dropout_func
    - PlotLayer
- loss
  - PixelDistanceLoss
  - StructuralSimilarityLoss
- models
  - LayoutContentDiscriminator 
  - PatchDiscriminator
  - ResNet
  - UNet
  - UNetDiscriminator
- optimizer
  - SWATS_ADAM
  - SWATS_NADAM
- regularization
  - CutMix
  - CutOut 
  - GetMask
- utils
  - DetectHw
  - EnableXlaAcceleration
  - EnableMixedPrecision

# Repo Stats
![](https://komarev.com/ghpvc/?username=saschakirchdeepsaki&color=yellow) since 16.04.2022
