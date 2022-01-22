# technnosaurs!

**DATABASE MANAGEMENT
**

We get a sample of media from each creator and tag the photos with some set of available characteristics. Each photographer has their own entry that is updated with each media's tags as they're inputted. We also store a list of available tags. Each row J of the database stores how many times each tag appears in creator J's profile.

Each photographer receives their own ID that the photo information can be pulled with. People can also add their own tags that future photos can be tagged with and current photos can be updated with as well.

**REC ALG
**

User inputs a list of tags that they are looking for (a vector of 1's and 0's). We output a N number of recommendations (modifiable).

First we normalize each creator's tag profile. Since the database stores how many times each tag appears for each creator, we take creator J, look at tag K, and take a ratio of how many times each tag appears for a creator overall divided by the square root of the number of entries total a creator has. The power of the divided number (e.g. 1/2 for square root) can be increased or decreased to granulate or blur data, respectively, as needed.

This granularity is enforced through a sigmoid function filter, where a sigmoid function centered around some theta (default 0.5) transforms the inputted data along a sigmoid curve, giving an output of between 0 and 1. However, to clear up noise, we apply a simple filter, where all inputs less than some phi (default 0.35) are instead outputted to 0.

The algorithm operates on each normalized profile similar to a sparse-data neighbors model. We find the dot product of the user tag input vector and each normalized row. We output the N closest fits. 

The way that we process the data prior to the sigmoid function filter puts a greater weight on users who submit lots of data, in accordance to a root-like curve (i.e. diminishing marginal returns the more are submitted). In other words, if 1/2 photos contain smiling people, that gets less value in the dot product than a photographer who submits 10/20 photos containing smiling people, though less than a factor of 10. This is further reduced via the sigmoid function, so that users who submit 9/10 photos with some tag are outputted nearly the same for that tag as users who submit 18/20 photos with some tag.
