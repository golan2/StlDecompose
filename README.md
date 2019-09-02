# StlDecompose
Playing with STL decomposing for finding the trend and seasonality

## STL for Sleeve
We run STL in order to decompose the data into its 3 components.
We set the baseline to be {trend+seasonality}.
We calculate the "height" of the sleeve acording to STD.

The STD can be calculated from all the data points (fixed std) or using a Moving STD.
We show several sleeves with different values of alpha for the MovingSTD.
