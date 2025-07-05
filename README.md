# FairBoardingQuantQuestion - Reservoir Sampling

Link to Youtube Video: https://www.youtube.com/watch?v=NXs6hijbqkI&list=PLADLdjl79_mhdmhdxA1Gk8sklGEWJkEKq&index=2

This questions has to do with designing an efficient reservoir sampling method that is both efficient and fair.

1. First Come First Serve: is fast because selection is decided immediately but doesn't give fair probability to all entities in reservoir

2. Random Selection: is fair because offers all entities the same probability, but is not efficient since without all entities being present, this sampling method cannot be performed

3. Optimal Solution: for entities 1 - n (want to select n entities), immediately select, and for each following kth entitiy, randomly select index between 1 - k, and if the index is between 1-n, replace selected n

See ipnyb file for visualization
