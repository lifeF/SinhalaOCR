"""
Rathnayake R.M.K.D
University of Peradeniya 
Faculty of Engineering 

INRUDUCTIONS
------------
Activation functions are really important for a Artificial Neural Network to learn and make sense of 
something really complicated and Non-linear complex functional mappings between the inputs and response
variable.They introduce non-linear properties to our Network.Their main purpose is to convert a input 
signal of a node in a A-NN to an output signal. That output signal now is used as a input in the 
next layer in the stack.

Specifically in A-NN we do the sum of products of inputs(X) and their corresponding Weights(W) and apply
a Activation function f(x) to it to get the output of that layer and feed it as an input to the next layer.

Most popular types of Activation functions
------------------------------------------
    ========================================================================================================================
    1) Sigmoid or Logistic
        Discription
        -----------
        f(x) = 1 / 1 + exp(-x) . Its Range is between 0 and 1. It is a S — shaped curve.
        It is easy to understand and apply but it has major reasons which have made it fall out of popularity
            > Vanishing gradient problem

            > Secondly , its output isn’t zero centered. It makes the gradient updates go too far in different directions. 
              0 < output < 1, and it makes optimization harder.

            > Sigmoids saturate and kill gradients.

            > Sigmoids have slow convergence.
    ========================================================================================================================
    2) Tanh — Hyperbolic tangent
        Discription
        -----------
        Hyperbolic Tangent function- Tanh : It’s mathamatical formula is f(x) = 1 — exp(-2x) / 1 + exp(-2x).
        Now it’s output is zero centered because its range in between -1 to 1 i.e -1 < output < 1 . Hence 
        optimization is easier in this method hence in practice it is always preferred over Sigmoid function . 
        But still it suffers from Vanishing gradient problem.
    ========================================================================================================================
    3) ReLu -Rectified linear units
        Discription
        -----------
         It has become very popular in the past couple of years. It was recently proved that it had 6 times improvement 
         in convergence from Tanh function. It’s just R(x) = max(0,x) i.e if x < 0 , R(x) = 0 and if x >= 0 , R(x) = x. 
         Hence as seeing the mathamatical form of this function we can see that it is very simple and efficinent . 
         A lot of times in Machine learning and computer science we notice that most simple and consistent techniques and 
         methods are only preferred and are best. Hence it avoids and rectifies vanishing gradient problem . Almost all 
         deep learning Models use ReLu nowadays.

    ========================================================================================================================
"""



class ActiveFunction:
    # Sigmoid or Logistic
    @staticmethod
    def Sigmoid(x):
        if 0 <=x & x <= 1 :
            return 1
        return 0

    @staticmethod
    def Logistic(x):
        if 0 <=x & x <= 1 :
            return 1
        return 0

    # Tanh — Hyperbolic tangent
    @staticmethod
    def ActiveFunction2(x):
        if 0 <=x & x <= 1 :
            return 1
        return 0

    # ReLu -Rectified linear units
   