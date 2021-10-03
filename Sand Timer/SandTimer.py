# Load the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from math import log10, floor


# Create some helper functions
def roundToNearest(x):
    """
    Rounds number to nearest significant digit. Returns (roundedNumber, decimalOfRounding)
    """
    return round(x, -int(floor(log10(abs(x))))), -int(floor(log10(abs(x))))

def CalculateAvgAndStd(data, dataName, unitName="", isRounded=True):
    """
    Parameters
    ----------
    data : 1D array
        Dataset to do calculations on (here order does not matter).
    dataName : string
        Name of dataset.
    unitName : string, optional
        The unit of measurement for the dataset. The default is "".
    isRounded : boolean, optional
        Rounds down std to first significant digit and rounds down average to same precision. The default is True.

    Returns
    -------
    average : float
        Average of dataset.
    std : float
        Standard deviation of dataset.
    """
    average = np.average(data)
    std = np.std(data)
    
    if isRounded:
        # Round
        std, decimal = roundToNearest(std)
        average = round(average, decimal)
    
    print("\tAverage of " + dataName + ": " + str(average) + " " + unitName)
    print("\tStd of " + dataName + ": " + str(std) + " " + unitName + "\n")
    
    return average, std


# TimerA.txt plot

# Load input data from file RateT.txt, comma separated
TimerAData = np.loadtxt("TimerA.txt", delimiter=",")

# Seperate data into which side is up T (1) or B (0)
timerATopUp, timerABottomUp = [], []

for i in range(len(TimerAData)):
    if TimerAData[i,2] == 1:
        timerATopUp += [TimerAData[i,1]]
    else:
        timerABottomUp += [TimerAData[i,1]]

# Make the plots for timer A data

# Plots without error bars, 'k.' plots as black points
timerAError = 10*[0.2]
timerATrials = list(range(1, 11))

plt.figure(1)
plt.errorbar(timerATrials, timerATopUp, timerAError, fmt='r+')
plt.errorbar(timerATrials, timerABottomUp, timerAError, fmt='b.')
plt.title('Fig. 1: Timer A')
plt.xlabel('Trial number')
plt.ylabel('Time of sand timer (in seconds)')
plt.legend(('Top Up (T)', 'Bottom Up (B)'))
plt.savefig('Figure1.png')
plt.show()

# Calculate the averages and standard deviations from the total and sub datasets
AData = TimerAData[:,1]
print("Timer A Statistics:")

print("\tTimer A Estimated Error: 0.2 s\n")

# Entire dataset
averageA, stdA = CalculateAvgAndStd(AData, "timer A", "s")

# Dataset for timer A when the top is up
averageATopUp, stdATopUp = CalculateAvgAndStd(timerATopUp, "timer A (Top Up)", "s")

# Dataset for timer A when the bottom is up
averageABottomUp, stdABottomUp = CalculateAvgAndStd(timerABottomUp, "timer A (Bottom Up)", "s")


# TimerB.txt plot

# Load input data from file RateT.txt, comma separated
TimerBData = np.loadtxt("TimerB.txt", delimiter=",")

# Seperate data into which side is up T (1) or B (0)
timerBTopUp, timerBBottomUp = [], []

for i in range(len(TimerBData)):
    if TimerBData[i,2] == 1:
        timerBTopUp += [TimerBData[i,1]]
    else:
        timerBBottomUp += [TimerBData[i,1]]

# Make the plots for timer B data

# Plots without error bars, 'k.' plots as black points
timerBError = 10*[0.1]
timerBTrials = list(range(1, 11))

plt.figure(2)
plt.errorbar(timerBTrials, timerBTopUp, timerBError, fmt='r+')
plt.errorbar(timerBTrials, timerBBottomUp, timerBError, fmt='b.')
plt.title('Fig. 2: Timer B')
plt.xlabel('Trial number')
plt.ylabel('Time of sand timer (in seconds)')
plt.legend(('Top Up (T)', 'Bottom Up (B)'))
plt.savefig('Figure2.png')
plt.show()

# Calculate the averages and standard deviations from the total and sub datasets
BData = TimerBData[:,1]
print("Timer B Statistics:")

print("\tTimer B Estimated Error: 0.1 s\n")

# Entire dataset
averageB, stdB = CalculateAvgAndStd(BData, "timer B", "s")

# Dataset for timer B when the top is up
averageBTopUp, stdBTopUp = CalculateAvgAndStd(timerBTopUp, "timer B (Top Up)", "s")

# Dataset for timer B when the bottom is up
averageBBottomUp, stdBBottomUp = CalculateAvgAndStd(timerBBottomUp, "timer B (Bottom Up)", "s")


# TimerAandB.txt plots

# Load input data from file RateT.txt, comma separated
TimerAandBData = np.loadtxt("TimerAandB.txt", delimiter=",")

# Seperate data into which side is up T (1) or B (0)
ATopBTop, ATopBBottom, ABottomBTop, ABottomBBottom = [], [], [], []

for i in range(len(TimerAandBData)):
    # If A is Top Up
    if TimerAandBData[i,2] == 1:
        # If B is Top Up
        if TimerAandBData[i,3] == 1:
            ATopBTop += [TimerAandBData[i,1]]
        # If B is Bottom Up
        else:
            ATopBBottom += [TimerAandBData[i,1]]
    # If A is Bottom Up
    else:
        # If B is Top Up
        if TimerAandBData[i,3] == 1:
            ABottomBTop += [TimerAandBData[i,1]]
        # If B is Bottom Up
        else:
            ABottomBBottom += [TimerAandBData[i,1]]

# Make the plots for timer A and B data

# First, let's do A top up and B top up
AandBError = 5*[0.10]
timerAandBTrials = list(range(1, 6))

plt.figure(3)
plt.errorbar(timerAandBTrials, ATopBTop, AandBError, fmt='r+')
plt.title('Fig. 3: Timer A and B, A=Top & B=Top')
plt.xlabel('Trial number')
plt.ylabel('Difference in time between A and B (in seconds)')
plt.savefig('Figure3.png')
plt.show()

print("Timer A and B Statistics:")
print("\tTimer A and B Error: 0.1 s\n")

# Calculate the averages and standard deviations from differences
print("Difference Between Timer A (Top Up) and Timer B (Top Up) Statistics:")

averageATopBTop, stdATopBTop = CalculateAvgAndStd(ATopBTop, "difference between A (Top Up) and B (Top Up)", "s")


# Let's do A top up and B bottom up

plt.figure(4)
plt.errorbar(timerAandBTrials, ATopBBottom, AandBError, fmt='b.')
plt.title('Fig. 4: Timer A and B, A=Top & B=Bottom')
plt.xlabel('Trial number')
plt.ylabel('Difference in time between A and B (in seconds)')
plt.savefig('Figure4.png')
plt.show()

# Calculate the averages and standard deviations from differences
print("Difference Between Timer A (Top Up) and Timer B (Bottom Up) Statistics:")

averageATopBBottom, stdATopBBottom = CalculateAvgAndStd(ATopBBottom, "difference between A (Top Up) and B (Bottom Up)", "s")


# Let's do A bottom up and B top up

plt.figure(5)
plt.errorbar(timerAandBTrials, ABottomBTop, AandBError, fmt='k.')
plt.title('Fig. 5: Timer A and B, A=Bottom & B=Top')
plt.xlabel('Trial number')
plt.ylabel('Difference in time between A and B (in seconds)')
plt.savefig('Figure5.png')
plt.show()

# Calculate the averages and standard deviations from differences
print("Difference Between Timer A (Bottom Up) and Timer B (Top Up) Statistics:")

averageABottomBTop, stdABottomBTop = CalculateAvgAndStd(ABottomBTop, "difference between A (Bottom Up) and B (Top Up)", "s")


# Finally, let's do A bottom up and B bottom up

plt.figure(6)
plt.errorbar(timerAandBTrials, ABottomBBottom, AandBError, fmt='k.')
plt.title('Fig. 6: Timer A and B, A=Bottom & B=Bottom')
plt.xlabel('Trial number')
plt.ylabel('Difference in time between A and B (in seconds)')
plt.savefig('Figure6.png')
plt.show()

# Calculate the averages and standard deviations from differences
print("Difference Between Timer A (Bottom Up) and Timer B (Bottom Up) Statistics:")

averageABottomBBottom, stdABottomBBottom = CalculateAvgAndStd(ABottomBBottom, "difference between A (Bottom Up) and B (Bottom Up)", "s")

