# Handwriting Generation with LSTMs

A recurrent neural network architecture with Long Short Term Memory to generate handwriting sequences. Based off [Grzego's work](https://github.com/Grzego/handwriting-generation) which is an implementation of Alex Graves' great paper on this [[Paper]](https://arxiv.org/abs/1308.0850).

Lot of parameter changes were made and certain features were cut because I didn't need them. Overall, performance of the model was sub-par. It fares well on relatively long sequences and is messed up if you feed it special characters.

For the curious, you can try it out as a local web app.

In your project folder, run:
`
    $ python app.py
`

The web app should now be accessible at http://127.0.0.1.