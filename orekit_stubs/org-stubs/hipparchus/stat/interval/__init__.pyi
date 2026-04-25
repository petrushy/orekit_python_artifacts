
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import typing



class BinomialProportion:
    """
    Utility methods to generate confidence intervals for a binomial proportion.
    
          - ` Binomial proportion confidence interval (Wikipedia)
            <http://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval>`
    """
    @staticmethod
    def getAgrestiCoullInterval(numberOfTrials: int, probabilityOfSuccess: float, confidenceLevel: float) -> 'ConfidenceInterval':
        """
        Create an Agresti-Coull binomial confidence interval for the true probability of success of an unknown binomial distribution with the given observed number of trials, probability of success and confidence level.
        
        Preconditions:
        
          - numberOfTrials must be positive
          - probabilityOfSuccess must be between 0 and 1 (inclusive)
          - confidenceLevel must be strictly between 0 and 1 (exclusive)
        
        
        Parameters:
            numberOfTrials (int): number of trials
            probabilityOfSuccess (double): observed probability of success
            confidenceLevel (double): desired probability that the true probability of success falls within the returned interval
        
        Returns:
            Confidence interval containing the probability of success with probability confidenceLevel
        
        Raises:
            hipparchus: if numberOfTrials <= 0.
            hipparchus: if probabilityOfSuccess is not in the interval [0, 1].
            hipparchus: if confidenceLevel is not in the interval (0, 1).
        
              - ` Agresti-Coull interval (Wikipedia)
                <http://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Agresti-Coull_Interval>`
        
        
        
        """
        ...
    @staticmethod
    def getClopperPearsonInterval(numberOfTrials: int, probabilityOfSuccess: float, confidenceLevel: float) -> 'ConfidenceInterval':
        """
        Create a Clopper-Pearson binomial confidence interval for the true probability of success of an unknown binomial distribution with the given observed number of trials, probability of success and confidence level.
        
        Preconditions:
        
          - numberOfTrials must be positive
          - probabilityOfSuccess must be between 0 and 1 (inclusive)
          - confidenceLevel must be strictly between 0 and 1 (exclusive)
        
        
        Parameters:
            numberOfTrials (int): number of trials
            probabilityOfSuccess (double): observed probability of success
            confidenceLevel (double): desired probability that the true probability of success falls within the returned interval
        
        Returns:
            Confidence interval containing the probability of success with probability confidenceLevel
        
        Raises:
            hipparchus: if numberOfTrials <= 0.
            hipparchus: if probabilityOfSuccess is not in the interval [0, 1].
            hipparchus: if confidenceLevel is not in the interval (0, 1).
        
              - ` Clopper-Pearson interval (Wikipedia)
                <http://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Clopper-Pearson_interval>`
        
        
        
        """
        ...
    @staticmethod
    def getNormalApproximationInterval(numberOfTrials: int, probabilityOfSuccess: float, confidenceLevel: float) -> 'ConfidenceInterval':
        """
        Create a binomial confidence interval using normal approximation for the true probability of success of an unknown binomial distribution with the given observed number of trials, probability of success and confidence level.
        
        Preconditions:
        
          - numberOfTrials must be positive
          - probabilityOfSuccess must be between 0 and 1 (inclusive)
          - confidenceLevel must be strictly between 0 and 1 (exclusive)
        
        
        Parameters:
            numberOfTrials (int): number of trials
            probabilityOfSuccess (double): observed probability of success
            confidenceLevel (double): desired probability that the true probability of success falls within the returned interval
        
        Returns:
            Confidence interval containing the probability of success with probability confidenceLevel
        
        Raises:
            hipparchus: if numberOfTrials <= 0.
            hipparchus: if probabilityOfSuccess is not in the interval [0, 1].
            hipparchus: if confidenceLevel is not in the interval (0, 1).
        
              - ` Normal approximation interval (Wikipedia)
                <http://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Normal_approximation_interval>`
        
        
        
        """
        ...
    @staticmethod
    def getWilsonScoreInterval(numberOfTrials: int, probabilityOfSuccess: float, confidenceLevel: float) -> 'ConfidenceInterval':
        """
        Create an Wilson score binomial confidence interval for the true probability of success of an unknown binomial distribution with the given observed number of trials, probability of success and confidence level.
        
        Preconditions:
        
          - numberOfTrials must be positive
          - probabilityOfSuccess must be between 0 and 1 (inclusive)
          - confidenceLevel must be strictly between 0 and 1 (exclusive)
        
        
        Parameters:
            numberOfTrials (int): number of trials
            probabilityOfSuccess (double): observed probability of success
            confidenceLevel (double): desired probability that the true probability of success falls within the returned interval
        
        Returns:
            Confidence interval containing the probability of success with probability confidenceLevel
        
        Raises:
            hipparchus: if numberOfTrials <= 0.
            hipparchus: if probabilityOfSuccess is not in the interval [0, 1].
            hipparchus: if confidenceLevel is not in the interval (0, 1).
        
              - ` Wilson score interval (Wikipedia)
                <http://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval>`
        
        
        
        """
        ...

class ConfidenceInterval:
    """
    Represents an interval estimate of a population parameter.
    """
    def __init__(self, lowerBound: float, upperBound: float, confidenceLevel: float):
        """
        Create a confidence interval with the given bounds and confidence level.
        
        Preconditions:
        
          - lower must be strictly less than upper
          - confidenceLevel must be strictly between 0 and 1 (exclusive)
        
        
        Parameters:
            lowerBound (double): lower endpoint of the interval
            upperBound (double): upper endpoint of the interval
            confidenceLevel (double): coverage probability
        
        Raises:
            hipparchus: if the preconditions are not met
        
        
        """
        ...
    def getConfidenceLevel(self) -> float:
        """
        Get asserted probability that the interval contains the population parameter.
        
        Returns:
            the asserted probability that the interval contains the population parameter
        
        
        """
        ...
    def getLowerBound(self) -> float:
        """
        Get lower endpoint of the interval.
        
        Returns:
            the lower endpoint of the interval
        
        
        """
        ...
    def getUpperBound(self) -> float:
        """
        Get upper endpoint of the interval.
        
        Returns:
            the upper endpoint of the interval
        
        
        """
        ...
    def toString(self) -> str:
        """
        Get String representation of the confidence interval.
        
        Overrides: toString in class Object
        
        Returns:
            String representation of the confidence interval
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.interval")``.

    BinomialProportion: typing.Type[BinomialProportion]
    ConfidenceInterval: typing.Type[ConfidenceInterval]
