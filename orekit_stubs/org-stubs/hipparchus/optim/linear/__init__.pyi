
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import jpype
import org.hipparchus.analysis
import org.hipparchus.linear
import org.hipparchus.optim
import org.hipparchus.optim.nonlinear.scalar
import typing



class LinearConstraint(java.io.Serializable):
    """
    A linear constraint for a linear optimization problem.
    
    * A linear constraint has one of the forms:
    
      - c :sub:`1` x :sub:`1` + ... c :sub:`n` x :sub:`n` = v
      - c :sub:`1` x :sub:`1` + ... c :sub:`n` x :sub:`n` <= v
      - c :sub:`1` x :sub:`1` + ... c :sub:`n` x :sub:`n` >= v
      - l :sub:`1` x :sub:`1` + ... l :sub:`n` x :sub:`n` + l :sub:`cst` = r :sub:`1` x :sub:`1` + ... r :sub:`n` x :sub:`n` + r
        :sub:`cst`
      - l :sub:`1` x :sub:`1` + ... l :sub:`n` x :sub:`n` + l :sub:`cst` <= r :sub:`1` x :sub:`1` + ... r :sub:`n` x :sub:`n` +
        r :sub:`cst`
      - l :sub:`1` x :sub:`1` + ... l :sub:`n` x :sub:`n` + l :sub:`cst` >= r :sub:`1` x :sub:`1` + ... r :sub:`n` x :sub:`n` +
        r :sub:`cst`
    
    The c :sub:`i` , l :sub:`i` or r :sub:`i` are the coefficients of the constraints, the x :sub:`i` are the coordinates of the current point and v is the value of the constraint.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self, lhsCoefficients: typing.Union[typing.List[float], jpype.JArray], lhsConstant: float, relationship: 'Relationship', rhsCoefficients: typing.Union[typing.List[float], jpype.JArray], rhsConstant: float): ...
    @typing.overload
    def __init__(self, coefficients: typing.Union[typing.List[float], jpype.JArray], relationship: 'Relationship', value: float): ...
    @typing.overload
    def __init__(self, lhsCoefficients: org.hipparchus.linear.RealVector, lhsConstant: float, relationship: 'Relationship', rhsCoefficients: org.hipparchus.linear.RealVector, rhsConstant: float): ...
    @typing.overload
    def __init__(self, coefficients: org.hipparchus.linear.RealVector, relationship: 'Relationship', value: float): ...
    def equals(self, other: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getCoefficients(self) -> org.hipparchus.linear.RealVector:
        """
        Gets the coefficients of the constraint (left hand side).
        
        Returns:
            the coefficients of the constraint (left hand side).
        
        
        """
        ...
    def getRelationship(self) -> 'Relationship':
        """
        Gets the relationship between left and right hand sides.
        
        Returns:
            the relationship between left and right hand sides.
        
        
        """
        ...
    def getValue(self) -> float:
        """
        Gets the value of the constraint (right hand side).
        
        Returns:
            the value of the constraint (right hand side).
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class LinearConstraintSet(org.hipparchus.optim.OptimizationData):
    """
    Class that represents a set of LinearConstraint.
    """
    @typing.overload
    def __init__(self, constraints: typing.Union[java.util.Collection[LinearConstraint], typing.Sequence[LinearConstraint], typing.Set[LinearConstraint]]): ...
    @typing.overload
    def __init__(self, *constraints: LinearConstraint): ...
    def getConstraints(self) -> java.util.Collection[LinearConstraint]:
        """
        Gets the set of linear constraints.
        
        Returns:
            the constraints.
        
        
        """
        ...

class LinearObjectiveFunction(org.hipparchus.analysis.MultivariateFunction, org.hipparchus.optim.OptimizationData, java.io.Serializable):
    """
    An objective function for a linear optimization problem.
    
    A linear objective function has one the form: \[ c_1 x_1 + \ldots c_n x_n + d \] The c :sub:`i` and d are the coefficients of the equation, the x :sub:`i` are the coordinates of the current point.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self, coefficients: typing.Union[typing.List[float], jpype.JArray], constantTerm: float): ...
    @typing.overload
    def __init__(self, coefficients: org.hipparchus.linear.RealVector, constantTerm: float): ...
    def equals(self, other: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getCoefficients(self) -> org.hipparchus.linear.RealVector:
        """
        Gets the coefficients of the linear equation being optimized.
        
        Returns:
            coefficients of the linear equation being optimized.
        
        
        """
        ...
    def getConstantTerm(self) -> float:
        """
        Gets the constant of the linear equation being optimized.
        
        Returns:
            constant of the linear equation being optimized.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    @typing.overload
    def value(self, point: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Computes the value of the linear equation at the current point.
        
        Specified by: hipparchus in interface hipparchus
        
        Parameters:
            point (double[]): Point at which linear equation must be evaluated.
        
        Returns:
            the value of the linear equation at the current point.
        
        Computes the value of the linear equation at the current point.
        
        Parameters:
            point (hipparchus): Point at which linear equation must be evaluated.
        
        Returns:
            the value of the linear equation at the current point.
        
        
        """
        ...
    @typing.overload
    def value(self, point: org.hipparchus.linear.RealVector) -> float: ...

class LinearOptimizer(org.hipparchus.optim.nonlinear.scalar.MultivariateOptimizer):
    """
    Base class for implementing linear optimizers.
    """
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optData: org.hipparchus.optim.OptimizationData) -> org.hipparchus.optim.PointValuePair: ...

class NonNegativeConstraint(org.hipparchus.optim.OptimizationData):
    """
    A constraint for a linear optimization problem indicating whether all variables must be restricted to non-negative values.
    """
    def __init__(self, restricted: bool):
        """
        Simple constructor.
        
        Parameters:
            restricted (boolean): If true, all the variables must be positive.
        
        
        """
        ...
    def isRestrictedToNonNegative(self) -> bool:
        """
        Indicates whether all the variables must be restricted to non-negative values.
        
        Returns:
            true if all the variables must be positive.
        
        
        """
        ...

class PivotSelectionRule(java.lang.Enum['PivotSelectionRule'], org.hipparchus.optim.OptimizationData):
    """
    Pivot selection rule to the use for a Simplex solver.
    """
    DANTZIG: typing.ClassVar['PivotSelectionRule'] = ...
    BLAND: typing.ClassVar['PivotSelectionRule'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'PivotSelectionRule':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['PivotSelectionRule']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (PivotSelectionRule c : PivotSelectionRule.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Relationship(java.lang.Enum['Relationship']):
    """
    Types of relationships between two cells in a Solver LinearConstraint.
    """
    EQ: typing.ClassVar['Relationship'] = ...
    LEQ: typing.ClassVar['Relationship'] = ...
    GEQ: typing.ClassVar['Relationship'] = ...
    def oppositeRelationship(self) -> 'Relationship':
        """
        Gets the relationship obtained when multiplying all coefficients by -1.
        
        Returns:
            the opposite relationship.
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Enum in class Enum
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'Relationship':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['Relationship']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (Relationship c : Relationship.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SolutionCallback(org.hipparchus.optim.OptimizationData):
    """
    A callback object that can be provided to a linear optimizer to keep track of the best solution found.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def getSolution(self) -> org.hipparchus.optim.PointValuePair:
        """
        Retrieve the best solution found so far.
        
        Note: the returned solution may not be optimal, e.g. in case the optimizer did reach the iteration limits.
        
        Returns:
            the best solution found so far by the optimizer, or null if no feasible solution could be found
        
        
        """
        ...
    def isSolutionOptimal(self) -> bool:
        """
        Returns if the found solution is optimal.
        
        Returns:
            true if the solution is optimal, false otherwise
        
        
        """
        ...

class SimplexSolver(LinearOptimizer):
    """
    Solves a linear problem using the "Two-Phase Simplex" method.
    
    The SimplexSolver supports the following OptimizationData data provided as arguments to optimize:
    
      - objective function: LinearObjectiveFunction - mandatory
      - linear constraints LinearConstraintSet - mandatory
      - type of optimization: GoalType - optional, default:
        MINIMIZE
      - whether to allow negative values as solution: NonNegativeConstraint - optional,
        default: true
      - pivot selection rule: PivotSelectionRule - optional, default
        DANTZIG
      - callback for the best solution: SolutionCallback - optional
      - maximum number of iterations: MaxIter - optional, default:
        Integer
    
    Note: Depending on the problem definition, the default convergence criteria may be too strict, resulting in hipparchus or hipparchus. In such a case it is advised to adjust these criteria with more appropriate values, e.g. relaxing the epsilon value.
    
    Default convergence criteria:
    
      - Algorithm convergence: 1e-6
      - Floating-point comparisons: 10 ulp
      - Cut-Off value: 1e-10
    
    The cut-off value has been introduced to handle the case of very small pivot elements in the Simplex tableau, as these may lead to numerical instabilities and degeneracy. Potential pivot elements smaller than this value will be treated as if they were zero and are thus not considered by the pivot selection mechanism. The default value is safe for many problems, but may need to be adjusted in case of very small coefficients used in either the LinearConstraint or LinearObjectiveFunction.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, epsilon: float): ...
    @typing.overload
    def __init__(self, epsilon: float, maxUlps: int): ...
    @typing.overload
    def __init__(self, epsilon: float, maxUlps: int, cutOff: float): ...
    def doOptimize(self) -> org.hipparchus.optim.PointValuePair:
        """
        Performs the bulk of the optimization algorithm.
        
        Specified by: doOptimize in class BaseOptimizer
        
        Returns:
            the point/value pair giving the optimal value of the objective function.
        
        Raises:
            hipparchus: 
        
        """
        ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optData: org.hipparchus.optim.OptimizationData) -> org.hipparchus.optim.PointValuePair: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim.linear")``.

    LinearConstraint: typing.Type[LinearConstraint]
    LinearConstraintSet: typing.Type[LinearConstraintSet]
    LinearObjectiveFunction: typing.Type[LinearObjectiveFunction]
    LinearOptimizer: typing.Type[LinearOptimizer]
    NonNegativeConstraint: typing.Type[NonNegativeConstraint]
    PivotSelectionRule: typing.Type[PivotSelectionRule]
    Relationship: typing.Type[Relationship]
    SimplexSolver: typing.Type[SimplexSolver]
    SolutionCallback: typing.Type[SolutionCallback]
