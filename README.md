# quadrants

Experiment with having creatures with neural network brains learn
to pick which area to move to.

There are 9 grid cells they choose from (so not actually
quadrants anymore).

![quadrants](https://user-images.githubusercontent.com/794661/27210210-c07657fe-521e-11e7-97c0-550e89bae0be.gif)

# what I learned

The creatures mostly only seemed to be able to learn to favor the top
left and bottom right cells, depending on what reward function I
used. I'm thinking because this is because those were the highest
and lowest location indices.

For future improvements I should probably represent the cell
locations as binary individual input neurons, as opposed to a
single decimal input neuron. The single decimal input neuron is
probably leading the network to "infer" that the cells' indices
are a meaningful continuous spectrum, as opposed to just being
arbitrary IDs, which they are.

Also, I'm wondering if the network is too simple to be able to
properly represent the necessary mathematical function that would
be able to favor a "midway" cell, i.e. a cell that's not at one
of the extremes. Seems like the network isn't able to represent
anything beyond a basic linear equation, where going in one
direction is always good and going in the other direction is
always bad.

# getting this running

- start a dummy webserver for serving the JSON file outputted by
  the simulation by running `python mytornado.py`.
  Unfortunately, using something like `Python -m
  SimpleHTTPServer` wasn't working because of CORS.
- start the actual web app with `npm install`, then `npm start`.
- start the simulation with `python nn.py`. It will run for 20
  iterations.
