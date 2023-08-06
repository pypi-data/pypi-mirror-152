# JTorch: 一个全兼容 PyTorch 接口的高性能动态编译深度学习框架

JTorch 是一个完全兼容 PyTorch 接口的深度学习框架，同时基于 Jittor 元算子与统一计算图特性的加持，实现高性能动态编译，同时，用户原来使用的PyTorch代码，不需要进行任何修改，即可加速运行。总结而言，JTorch具有以下几点优势：

1. 零成本：完全兼容原生 PyTorch 接口， 用户代码不需要作任何更改。
2. 速度快：通过统一计算图执行方法，JTorch可以实现对代码的动态编译以及加速，相比原版 PyTorch拥有更好的性能。
3. 支持硬件多：JTorch底层通过元算子抽象，可以快速兼容适配多种人工智能芯片。
4. 兼容生态： 对原有 PyTorch 生态形成兼容，如各种第三方开发的 PyTorch 模型库。
5. 兼容计图： JTorch完全兼容计图，计图中的接口可以混合使用，性能高。
6. 完全自主可控： JTorch 具有完全的自主知识产权，用户完全不需要安装 Torch，即可直接使用。


JTorch相关连接：

*  [Github](https://github.com/JITTorch/jtorch)
*  [Jittor 论坛](https://discuss.jittor.org/)
*  即时通信: QQ Group(761222083)