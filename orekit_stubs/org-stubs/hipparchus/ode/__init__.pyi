
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import jpype
import org.hipparchus
import org.hipparchus.complex
import org.hipparchus.exception
import org.hipparchus.ode.events
import org.hipparchus.ode.nonstiff
import org.hipparchus.ode.sampling
import typing



class ComplexODEConverter:
    """
    This class converts ComplexOrdinaryDifferentialEquation into OrdinaryDifferentialEquation.
    
    This class is a wrapper around a ComplexOrdinaryDifferentialEquation which allow to use a ODEIntegrator to integrate it.
    
    The transformation is done by changing the n dimension state vector to a 2n dimension vector, where the even components are real parts and odd components are imaginary parts.
    
    One should be aware that the data is duplicated during the transformation process and that for each call to computeDerivatives, this wrapper does copy 4n scalars : 2n before the call to computeDerivatives in order to dispatch the y state vector, and 2n after the call to gather zDot. Since the underlying problem by itself perhaps also needs to copy data and dispatch the arrays into domain objects, this has an impact on both memory and CPU usage. The only way to avoid this duplication is to perform the transformation at the problem level, i.e. to implement the problem as a first order one and then avoid using this class.
    
    The proper way to use the converter is as follows:
    
    
       ODEIntegrator                       integrator       = ...build some integrator...;
       ComplexOrdinaryDifferentialEquation complexEquations = ...set up the complex problem...;
       ComplexODEState                     initialState     = ...set up initial state...;
       ComplexODEConverter                 converter        = new ComplexODEConverter();
       ComplexODEStateAndDerivative        finalstate       =
          converter.convertStateAndDerivative(integrator.integrate(converter.convertEquations(complexEquations),
                                                                   converter.convertState(initialState),
                                                                   t);
     
    
    If there are ComplexSecondaryODE, they must be converted too and both the converted primary equations and converted secondary equations must be combined together using ExpandableODE as usual for regular real equations.
    
    Since:
        1.4
    
    Also see:
        ComplexOrdinaryDifferentialEquation,
        OrdinaryDifferentialEquation
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def convertEquations(self, equations: 'ComplexOrdinaryDifferentialEquation') -> 'OrdinaryDifferentialEquation':
        """
        Convert an equations set.
        
        Parameters:
            equations (ComplexOrdinaryDifferentialEquation): equations to convert
        
        Returns:
            converted equations
        
        
        """
        ...
    def convertSecondaryEquations(self, equations: 'ComplexSecondaryODE') -> 'SecondaryODE':
        """
        Convert a secondary equations set.
        
        Parameters:
            equations (ComplexSecondaryODE): equations to convert
        
        Returns:
            converted equations
        
        
        """
        ...
    @typing.overload
    def convertState(self, state: 'ODEStateAndDerivative') -> 'ComplexODEStateAndDerivative':
        """
        Parameters:
            state (ComplexODEState): state to convert
        
        Returns:
            converted state
        
        Convert a real state and derivatives (typically the final state or some intermediate state for step handling or event handling).
        
        Parameters:
            state (ODEStateAndDerivative): state to convert
        
        Returns:
            converted state
        
        
        """
        ...
    @typing.overload
    def convertState(self, state: 'ComplexODEState') -> 'ODEState': ...

class ComplexODEState(java.io.Serializable):
    """
    Container for time, main and secondary state vectors.
    
    Since:
        1.4
    
    Also see:
        ComplexOrdinaryDifferentialEquation, SecondaryODE,
        ODEIntegrator, ODEStateAndDerivative, serialized
    """
    @typing.overload
    def __init__(self, time: float, primaryState: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray]): ...
    @typing.overload
    def __init__(self, time: float, primaryState: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], secondaryState: typing.Union[typing.List[typing.MutableSequence[org.hipparchus.complex.Complex]], jpype.JArray]): ...
    def getCompleteState(self) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
        Get complete state at time.
        
        Returns:
            complete state at time, starting with getPrimaryState, followed by all
            getSecondaryState in increasing index order
        
        Also see:
            getPrimaryState,
            getSecondaryState
        
        
        """
        ...
    def getCompleteStateDimension(self) -> int:
        """
        Return the dimension of the complete set of equations.
        
        The complete set of equations correspond to the primary set plus all secondary sets.
        
        Returns:
            dimension of the complete set of equations
        
        Also see:
            getPrimaryStateDimension,
            getSecondaryStateDimension
        
        
        """
        ...
    def getNumberOfSecondaryStates(self) -> int:
        """
        Get the number of secondary states.
        
        Returns:
            number of secondary states.
        
        
        """
        ...
    def getPrimaryState(self) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
        Get primary state at time.
        
        Returns:
            primary state at time
        
        Also see:
            getSecondaryState,
            getCompleteState
        
        
        """
        ...
    def getPrimaryStateDimension(self) -> int:
        """
        Get primary state dimension.
        
        Returns:
            primary state dimension
        
        Also see:
            getSecondaryStateDimension,
            getCompleteStateDimension
        
        
        """
        ...
    def getSecondaryState(self, index: int) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
        Get secondary state at time.
        
        Parameters:
            index (int): index of the secondary set as returned by addSecondaryEquations (beware index
                0 corresponds to primary state, secondary states start at 1)
        
        Returns:
            secondary state at time
        
        Also see:
            getPrimaryState,
            getCompleteState
        
        
        """
        ...
    def getSecondaryStateDimension(self, index: int) -> int:
        """
        Get secondary state dimension.
        
        Parameters:
            index (int): index of the secondary set as returned by addSecondaryEquations (beware index
                0 corresponds to primary state, secondary states start at 1)
        
        Returns:
            secondary state dimension
        
        Also see:
            getPrimaryStateDimension,
            getCompleteStateDimension
        
        
        """
        ...
    def getTime(self) -> float:
        """
        Get time.
        
        Returns:
            time
        
        
        """
        ...

class ComplexOrdinaryDifferentialEquation:
    """
    This interface represents a first order differential equations set for hipparchus.
    
    Since:
        1.4
    
    Also see:
        OrdinaryDifferentialEquation, ComplexODEConverter
    """
    def computeDerivatives(self, t: float, y: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray]) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
        Get the current time derivative of the state vector.
        
        Parameters:
            t (double): current value of the independent time variable
            y (hipparchus[]): array containing the current value of the state vector
        
        Returns:
            time derivative of the state vector
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the problem.
        
        Returns:
            dimension of the problem
        
        
        """
        ...
    def init(self, t0: float, y0: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], finalTime: float) -> None:
        """
        Initialize equations at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the equations to initialize some internal data if needed.
        
        The default implementation does nothing.
        
        Parameters:
            t0 (double): value of the independent time variable at integration start
            y0 (hipparchus[]): array containing the value of the state vector at integration start
            finalTime (double): target time for the integration
        
        
        """
        ...

class ComplexSecondaryODE:
    """
    This interface allows users to add secondary differential equations to a primary set of differential equations.
    
    In some cases users may need to integrate some problem-specific equations along with a primary set of differential equations. One example is optimal control where adjoined parameters linked to the minimized hamiltonian must be integrated.
    
    This interface allows users to add such equations to a primary set of OrdinaryDifferentialEquation thanks to the addSecondaryEquations method, after having converted the instance to SecondaryODE
    
    Since:
        1.4
    
    Also see:
        ExpandableODE, ComplexODEConverter
    """
    def computeDerivatives(self, t: float, primary: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], primaryDot: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], secondary: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray]) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
        Compute the derivatives related to the secondary state parameters.
        
        In some cases, additional equations can require to change the derivatives of the primary state (i.e. the content of the primaryDot array). One use case is optimal control, when the secondary equations handle co-state, which changes control, and the control changes the primary state. In this case, the primary and secondary equations are not really independent from each other, so if possible it would be better to put state and co-state and their equations all in the primary equations. As this is not always possible, this method explicitly allows to modify the content of the primaryDot array. This array will be used to evolve the primary state only after all secondary equations have computed their derivatives, hence allowing this side effect.
        
        Parameters:
            t (double): current value of the independent time variable
            primary (hipparchus[]): array containing the current value of the primary state vector
            primaryDot (hipparchus[]): array containing the derivative of the primary state vector (the method is allowed to change the derivatives here, when
                the additional equations do have an effect on the primary equations)
            secondary (hipparchus[]): array containing the current value of the secondary state vector
        
        Returns:
            derivative of the secondary state vector
        
        Raises:
            hipparchus: if the number of functions evaluations is exceeded
            hipparchus: if arrays dimensions do not match equations settings
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the secondary state parameters.
        
        Returns:
            dimension of the secondary state parameters
        
        
        """
        ...
    def init(self, t0: float, primary0: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], secondary0: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], finalTime: float) -> None:
        """
        Initialize equations at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the equations to initialize some internal data if needed.
        
        The default implementation does nothing.
        
        Parameters:
            t0 (double): value of the independent time variable at integration start
            primary0 (hipparchus[]): array containing the value of the primary state vector at integration start
            secondary0 (hipparchus[]): array containing the value of the secondary state vector at integration start
            finalTime (double): target time for the integration
        
        
        """
        ...

class DenseOutputModel(org.hipparchus.ode.sampling.ODEStepHandler, java.io.Serializable):
    """
    This class stores all information provided by an ODE integrator during the integration process and build a continuous model of the solution from this.
    
    This class act as a step handler from the integrator point of view. It is called iteratively during the integration process and stores a copy of all steps information in a sorted collection for later use. Once the integration process is over, the user can use the getInterpolatedState method to retrieve this information at any time. It is important to wait for the integration to be over before attempting to call getInterpolatedState because some internal variables are set only once the last step has been handled.
    
    This is useful for example if the main loop of the user application should remain independent from the integration process or if one needs to mimic the behaviour of an analytical model despite a numerical model is used (i.e. one needs the ability to get the model value at any time or to navigate through the data).
    
    If problem modeling is done with several separate integration phases for contiguous intervals, the same DenseOutputModel can be used as step handler for all integration phases as long as they are performed in order and in the same direction. As an example, one can extrapolate the trajectory of a satellite with one model (i.e. one set of differential equations) up to the beginning of a maneuver, use another more complex model including thrusters modeling and accurate attitude control during the maneuver, and revert to the first model after the end of the maneuver. If the same continuous output model handles the steps of all integration phases, the user do not need to bother when the maneuver begins or ends, he has all the data available in a transparent manner.
    
    An important feature of this class is that it implements the Serializable interface. This means that the result of an integration can be serialized and reused later (if stored into a persistent medium like a filesystem or a database) or elsewhere (if sent to another application). Only the result of the integration is stored, there is no reference to the integrated problem by itself.
    
    One should be aware that the amount of data stored in a DenseOutputModel instance can be important if the state vector is large, if the integration interval is long or if the steps are small (which can result from small tolerance settings in AdaptiveStepsizeIntegrator).
    
    Also see:
        ODEStepHandler, ODEStateInterpolator,
        serialized
    """
    def __init__(self):
        """
        Simple constructor. Build an empty continuous output model.
        """
        ...
    def append(self, model: 'DenseOutputModel') -> None:
        """
        Append another model at the end of the instance.
        
        Parameters:
            model (DenseOutputModel): model to add at the end of the instance
        
        Raises:
            hipparchus: if the model to append is not compatible with the instance (dimension of the state vector, propagation direction, hole
                between the dates)
            hipparchus: if the number of functions evaluations is exceeded during step finalization
        
        
        """
        ...
    def finish(self, finalState: 'ODEStateAndDerivative') -> None:
        """
        Finalize integration.
        
        Specified by: finish in interface ODEStepHandler
        
        Parameters:
            finalState (ODEStateAndDerivative): state at integration end
        
        
        """
        ...
    def getFinalTime(self) -> float:
        """
        Get the final integration time.
        
        Returns:
            final integration time
        
        
        """
        ...
    def getInitialTime(self) -> float:
        """
        Get the initial integration time.
        
        Returns:
            initial integration time
        
        
        """
        ...
    def getInterpolatedState(self, time: float) -> 'ODEStateAndDerivative':
        """
        Get the state at interpolated time.
        
        Parameters:
            time (double): time of the interpolated point
        
        Returns:
            state at interpolated time
        
        
        """
        ...
    def handleStep(self, interpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> None:
        """
        Handle the last accepted step.
        
        Specified by: handleStep in interface ODEStepHandler
        
        Parameters:
            interpolator (ODEStateInterpolator): interpolator for the last accepted step
        
        
        """
        ...
    def init(self, initialState: 'ODEStateAndDerivative', targetTime: float) -> None:
        """
        Initialize step handler at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the step handler to initialize some internal data if needed.
        
        The default implementation does nothing
        
        Specified by: init in interface ODEStepHandler
        
        Parameters:
            initialState (ODEStateAndDerivative): initial time, state vector and derivative
            targetTime (double): target time for the integration
        
        
        """
        ...

class EquationsMapper(java.io.Serializable):
    """
    Class mapping the part of a complete state or derivative that pertains to a specific differential equation.
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        SecondaryODE, serialized
    """
    def extractEquationData(self, index: int, complete: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Extract equation data from a complete state or derivative array.
        
        Parameters:
            index (int): index of the equation, must be between 0 included and getNumberOfEquations
                (excluded)
            complete (double[]): complete state or derivative array from which equation data should be retrieved
        
        Returns:
            equation data
        
        Raises:
            hipparchus: if index is out of range
            hipparchus: if complete state has not enough elements
        
        
        """
        ...
    def getNumberOfEquations(self) -> int:
        """
        Get the number of equations mapped.
        
        Returns:
            number of equations mapped
        
        
        """
        ...
    def getTotalDimension(self) -> int:
        """
        Return the dimension of the complete set of equations.
        
        The complete set of equations correspond to the primary set plus all secondary sets.
        
        Returns:
            dimension of the complete set of equations
        
        
        """
        ...
    def insertEquationData(self, index: int, equationData: typing.Union[typing.List[float], jpype.JArray], complete: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Insert equation data into a complete state or derivative array.
        
        Parameters:
            index (int): index of the equation, must be between 0 included and getNumberOfEquations
                (excluded)
            equationData (double[]): equation data to be inserted into the complete array
            complete (double[]): placeholder where to put equation data (only the part corresponding to the equation will be overwritten)
        
        Raises:
            hipparchus: if either array has not enough elements
        
        
        """
        ...
    def mapStateAndDerivative(self, t: float, y: typing.Union[typing.List[float], jpype.JArray], yDot: typing.Union[typing.List[float], jpype.JArray]) -> 'ODEStateAndDerivative':
        """
        Map flat arrays to a state and derivative.
        
        Parameters:
            t (double): time
            y (double[]): state array to map, including primary and secondary components
            yDot (double[]): state derivative array to map, including primary and secondary components
        
        Returns:
            mapped state
        
        Raises:
            hipparchus: if an array does not match total dimension
        
        
        """
        ...

class ExpandableODE:
    """
    This class represents a combined set of first order differential equations, with at least a primary set of equations expandable by some sets of secondary equations.
    
    One typical use case is the computation of the Jacobian matrix for some ODE. In this case, the primary set of equations corresponds to the raw ODE, and we add to this set another bunch of secondary equations which represent the Jacobian matrix of the primary set.
    
    We want the integrator to use only the primary set to estimate the errors and hence the step sizes. It should not use the secondary equations in this computation. The AbstractIntegrator will be able to know where the primary set ends and so where the secondary sets begin.
    
    Also see:
        OrdinaryDifferentialEquation, VariationalEquation
    """
    def __init__(self, primary: 'OrdinaryDifferentialEquation'):
        """
        Build an expandable set from its primary ODE set.
        
        Parameters:
            primary (OrdinaryDifferentialEquation): the primary set of differential equations to be integrated.
        
        
        """
        ...
    def addSecondaryEquations(self, secondary: 'SecondaryODE') -> int:
        """
        Add a set of secondary equations to be integrated along with the primary set.
        
        Parameters:
            secondary (SecondaryODE): secondary equations set
        
        Returns:
            index of the secondary equation in the expanded state, to be used as the parameter to
            getSecondaryState and
            getSecondaryDerivative (beware index 0 corresponds to primary
            state, secondary states start at 1)
        
        
        """
        ...
    def computeDerivatives(self, t: float, y: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Get the current time derivative of the complete state vector.
        
        Parameters:
            t (double): current value of the independent time variable
            y (double[]): array containing the current value of the complete state vector
        
        Returns:
            time derivative of the complete state vector
        
        Raises:
            hipparchus: if the number of functions evaluations is exceeded
            hipparchus: if arrays dimensions do not match equations settings
        
        
        """
        ...
    def getMapper(self) -> EquationsMapper:
        """
        Get the mapper for the set of equations.
        
        Returns:
            mapper for the set of equations
        
        
        """
        ...
    def getPrimary(self) -> 'OrdinaryDifferentialEquation':
        """
        Get the primary set of differential equations to be integrated.
        
        Returns:
            primary set of differential equations to be integrated
        
        
        """
        ...
    def init(self, s0: 'ODEState', finalTime: float) -> None:
        """
        Initialize equations at the start of an ODE integration.
        
        Parameters:
            s0 (ODEState): state at integration start
            finalTime (double): target time for the integration
        
        Raises:
            hipparchus: if the number of functions evaluations is exceeded
            hipparchus: if arrays dimensions do not match equations settings
        
        
        """
        ...

_FieldDenseOutputModel__T = typing.TypeVar('_FieldDenseOutputModel__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDenseOutputModel(org.hipparchus.ode.sampling.FieldODEStepHandler[_FieldDenseOutputModel__T], typing.Generic[_FieldDenseOutputModel__T]):
    """
    This class stores all information provided by an ODE integrator during the integration process and build a continuous model of the solution from this.
    
    This class act as a step handler from the integrator point of view. It is called iteratively during the integration process and stores a copy of all steps information in a sorted collection for later use. Once the integration process is over, the user can use the getInterpolatedState method to retrieve this information at any time. It is important to wait for the integration to be over before attempting to call getInterpolatedState because some internal variables are set only once the last step has been handled.
    
    This is useful for example if the main loop of the user application should remain independent from the integration process or if one needs to mimic the behaviour of an analytical model despite a numerical model is used (i.e. one needs the ability to get the model value at any time or to navigate through the data).
    
    If problem modeling is done with several separate integration phases for contiguous intervals, the same FieldDenseOutputModel can be used as step handler for all integration phases as long as they are performed in order and in the same direction. As an example, one can extrapolate the trajectory of a satellite with one model (i.e. one set of differential equations) up to the beginning of a maneuver, use another more complex model including thrusters modeling and accurate attitude control during the maneuver, and revert to the first model after the end of the maneuver. If the same continuous output model handles the steps of all integration phases, the user do not need to bother when the maneuver begins or ends, he has all the data available in a transparent manner.
    
    One should be aware that the amount of data stored in a FieldDenseOutputModel instance can be important if the state vector is large, if the integration interval is long or if the steps are small (which can result from small tolerance settings in AdaptiveStepsizeFieldIntegrator).
    
    Also see:
        FieldODEStepHandler,
        FieldODEStateInterpolator
    """
    def __init__(self):
        """
        Simple constructor. Build an empty continuous output model.
        """
        ...
    def append(self, model: 'FieldDenseOutputModel'[_FieldDenseOutputModel__T]) -> None:
        """
        Append another model at the end of the instance.
        
        Parameters:
            model (FieldDenseOutputModel<FieldDenseOutputModel> model): model to add at the end of the instance
        
        Raises:
            hipparchus: if the model to append is not compatible with the instance (dimension of the state vector, propagation direction, hole
                between the dates)
            hipparchus: if the dimensions of the states or the number of secondary states do not match
            hipparchus: if the number of functions evaluations is exceeded during step finalization
        
        
        """
        ...
    def finish(self, finalState: 'FieldODEStateAndDerivative'[_FieldDenseOutputModel__T]) -> None:
        """
        Finalize integration.
        
        Specified by: finish in interface FieldODEStepHandler
        
        Parameters:
            finalState (FieldODEStateAndDerivative<FieldDenseOutputModel> finalState): state at integration end
        
        
        """
        ...
    def getFinalTime(self) -> _FieldDenseOutputModel__T:
        """
        Get the final integration time.
        
        Returns:
            final integration time
        
        
        """
        ...
    def getInitialTime(self) -> _FieldDenseOutputModel__T:
        """
        Get the initial integration time.
        
        Returns:
            initial integration time
        
        
        """
        ...
    def getInterpolatedState(self, time: _FieldDenseOutputModel__T) -> 'FieldODEStateAndDerivative'[_FieldDenseOutputModel__T]:
        """
        Get the state at interpolated time.
        
        Parameters:
            time (FieldDenseOutputModel): time of the interpolated point
        
        Returns:
            state at interpolated time
        
        
        """
        ...
    def handleStep(self, interpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldDenseOutputModel__T]) -> None:
        """
        Handle the last accepted step.
        
        Specified by: handleStep in interface FieldODEStepHandler
        
        Parameters:
            interpolator (FieldODEStateInterpolator<FieldDenseOutputModel> interpolator): interpolator for the last accepted step
        
        
        """
        ...
    def init(self, initialState: 'FieldODEStateAndDerivative'[_FieldDenseOutputModel__T], t: _FieldDenseOutputModel__T) -> None:
        """
        Initialize step handler at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the step handler to initialize some internal data if needed.
        
        The default implementation does nothing.
        
        Specified by: init in interface FieldODEStepHandler
        
        Parameters:
            initialState (FieldODEStateAndDerivative<FieldDenseOutputModel> initialState): initial time, state vector and derivative
            t (FieldDenseOutputModel): target time for the integration
        
        
        """
        ...

_FieldEquationsMapper__T = typing.TypeVar('_FieldEquationsMapper__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEquationsMapper(java.io.Serializable, typing.Generic[_FieldEquationsMapper__T]):
    """
    Class mapping the part of a complete state or derivative that pertains to a set of differential equations.
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        FieldExpandableODE, serialized
    """
    def extractEquationData(self, index: int, complete: typing.Union[typing.List[_FieldEquationsMapper__T], jpype.JArray]) -> typing.MutableSequence[_FieldEquationsMapper__T]:
        """
        Extract equation data from a complete state or derivative array.
        
        Parameters:
            index (int): index of the equation, must be between 0 included and
                getNumberOfEquations (excluded)
            complete (FieldEquationsMapper[]): complete state or derivative array from which equation data should be retrieved
        
        Returns:
            equation data
        
        Raises:
            hipparchus: if index is out of range
            hipparchus: if complete state has not enough elements
        
        
        """
        ...
    def getNumberOfEquations(self) -> int:
        """
        Get the number of equations mapped.
        
        Returns:
            number of equations mapped
        
        
        """
        ...
    def getTotalDimension(self) -> int:
        """
        Return the dimension of the complete set of equations.
        
        The complete set of equations correspond to the primary set plus all secondary sets.
        
        Returns:
            dimension of the complete set of equations
        
        
        """
        ...
    def insertEquationData(self, index: int, equationData: typing.Union[typing.List[_FieldEquationsMapper__T], jpype.JArray], complete: typing.Union[typing.List[_FieldEquationsMapper__T], jpype.JArray]) -> None:
        """
        Insert equation data into a complete state or derivative array.
        
        Parameters:
            index (int): index of the equation, must be between 0 included and
                getNumberOfEquations (excluded)
            equationData (FieldEquationsMapper[]): equation data to be inserted into the complete array
            complete (FieldEquationsMapper[]): placeholder where to put equation data (only the part corresponding to the equation will be overwritten)
        
        Raises:
            hipparchus: if either array has not enough elements
        
        
        """
        ...
    def mapStateAndDerivative(self, t: _FieldEquationsMapper__T, y: typing.Union[typing.List[_FieldEquationsMapper__T], jpype.JArray], yDot: typing.Union[typing.List[_FieldEquationsMapper__T], jpype.JArray]) -> 'FieldODEStateAndDerivative'[_FieldEquationsMapper__T]:
        """
        Map flat arrays to a state and derivative.
        
        Parameters:
            t (FieldEquationsMapper): time
            y (FieldEquationsMapper[]): state array to map, including primary and secondary components
            yDot (FieldEquationsMapper[]): state derivative array to map, including primary and secondary components
        
        Returns:
            mapped state
        
        Raises:
            hipparchus: if an array does not match total dimension
        
        
        """
        ...

_FieldExpandableODE__T = typing.TypeVar('_FieldExpandableODE__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldExpandableODE(typing.Generic[_FieldExpandableODE__T]):
    """
    This class represents a combined set of first order differential equations, with at least a primary set of equations expandable by some sets of secondary equations.
    
    One typical use case is the computation of the Jacobian matrix for some ODE. In this case, the primary set of equations corresponds to the raw ODE, and we add to this set another bunch of secondary equations which represent the Jacobian matrix of the primary set.
    
    We want the integrator to use only the primary set to estimate the errors and hence the step sizes. It should not use the secondary equations in this computation. The FieldODEIntegrator will be able to know where the primary set ends and so where the secondary sets begin.
    
    Also see:
        FieldOrdinaryDifferentialEquation, FieldSecondaryODE
    """
    def __init__(self, primary: 'FieldOrdinaryDifferentialEquation'[_FieldExpandableODE__T]):
        """
        Build an expandable set from its primary ODE set.
        
        Parameters:
            primary (FieldOrdinaryDifferentialEquation<FieldExpandableODE> primary): the primary set of differential equations to be integrated.
        
        
        """
        ...
    def addSecondaryEquations(self, secondary: 'FieldSecondaryODE'[_FieldExpandableODE__T]) -> int:
        """
        Add a set of secondary equations to be integrated along with the primary set.
        
        Parameters:
            secondary (FieldSecondaryODE<FieldExpandableODE> secondary): secondary equations set
        
        Returns:
            index of the secondary equation in the expanded state, to be used as the parameter to
            getSecondaryState and
            getSecondaryDerivative (beware index 0 corresponds to primary
            state, secondary states start at 1)
        
        
        """
        ...
    def computeDerivatives(self, t: _FieldExpandableODE__T, y: typing.Union[typing.List[_FieldExpandableODE__T], jpype.JArray]) -> typing.MutableSequence[_FieldExpandableODE__T]:
        """
        Get the current time derivative of the complete state vector.
        
        Parameters:
            t (FieldExpandableODE): current value of the independent time variable
            y (FieldExpandableODE[]): array containing the current value of the complete state vector
        
        Returns:
            time derivative of the complete state vector
        
        Raises:
            hipparchus: if the number of functions evaluations is exceeded
            hipparchus: if arrays dimensions do not match equations settings
        
        
        """
        ...
    def getMapper(self) -> FieldEquationsMapper[_FieldExpandableODE__T]:
        """
        Get the mapper for the set of equations.
        
        Returns:
            mapper for the set of equations
        
        
        """
        ...
    def getPrimary(self) -> 'FieldOrdinaryDifferentialEquation'[_FieldExpandableODE__T]:
        """
        Get the primary set of differential equations to be integrated.
        
        Returns:
            primary set of differential equations to be integrated
        
        Since:
            2.2
        
        
        """
        ...
    def init(self, s0: 'FieldODEState'[_FieldExpandableODE__T], finalTime: _FieldExpandableODE__T) -> None:
        """
        Initialize equations at the start of an ODE integration.
        
        Parameters:
            s0 (FieldODEState<FieldExpandableODE> s0): state at integration start
            finalTime (FieldExpandableODE): target time for the integration
        
        Raises:
            hipparchus: if the number of functions evaluations is exceeded
            hipparchus: if arrays dimensions do not match equations settings
        
        
        """
        ...

_FieldODEIntegrator__T = typing.TypeVar('_FieldODEIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEIntegrator(typing.Generic[_FieldODEIntegrator__T]):
    """
    This interface represents a first order integrator for differential equations.
    
    The classes which are devoted to solve first order differential equations should implement this interface. The problems which can be handled should implement the FieldOrdinaryDifferentialEquation interface.
    
    Also see:
        FieldOrdinaryDifferentialEquation
    """
    def addEventDetector(self, detector: org.hipparchus.ode.events.FieldODEEventDetector[_FieldODEIntegrator__T]) -> None:
        """
        Add an event detector to the integrator.
        
        Parameters:
            detector (FieldODEEventDetector<FieldODEIntegrator> detector): event detector
        
        Since:
            3.0
        
        Also see:
            getEventDetectors,
            clearEventDetectors
        
        
        """
        ...
    def addStepEndHandler(self, handler: typing.Union[org.hipparchus.ode.events.FieldODEStepEndHandler[_FieldODEIntegrator__T], typing.Callable[['FieldODEStateAndDerivative'[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]]) -> None:
        """
        Add a handler for step ends to the integrator.
        
        The stepEndOccurred method of the handler will be called at each step end.
        
        Parameters:
            handler (FieldODEStepEndHandler<FieldODEIntegrator> handler): handler for step ends
        
        Since:
            3.0
        
        Also see:
            getStepEndHandlers,
            clearStepEndHandlers
        
        
        """
        ...
    def addStepHandler(self, handler: typing.Union[org.hipparchus.ode.sampling.FieldODEStepHandler[_FieldODEIntegrator__T], typing.Callable[[org.hipparchus.ode.sampling.FieldODEStateInterpolator[org.hipparchus.CalculusFieldElement]], None]]) -> None:
        """
        Add a step handler to this integrator.
        
        The handler will be called by the integrator for each accepted step.
        
        Parameters:
            handler (FieldODEStepHandler<FieldODEIntegrator> handler): handler for the accepted steps
        
        Also see:
            getStepHandlers,
            clearStepHandlers
        
        
        """
        ...
    def clearEventDetectors(self) -> None:
        """
        Remove all the event handlers that have been added to the integrator.
        
        Since:
            3.0
        
        Also see:
            addEventDetector,
            getEventDetectors
        
        
        """
        ...
    def clearStepEndHandlers(self) -> None:
        """
        Remove all the handlers for step ends that have been added to the integrator.
        
        Since:
            3.0
        
        Also see:
            addStepEndHandler,
            getStepEndHandlers
        
        
        """
        ...
    def clearStepHandlers(self) -> None:
        """
        Remove all the step handlers that have been added to the integrator.
        
        Also see:
            addStepHandler,
            getStepHandlers
        
        
        """
        ...
    def getCurrentSignedStepsize(self) -> _FieldODEIntegrator__T:
        """
        Get the current signed value of the integration stepsize.
        
        This method can be called during integration (typically by the object implementing the FieldOrdinaryDifferentialEquation problem) if the signed value of the current stepsize that is tried is needed.
        
        The result is undefined if the method is called outside of calls to integrate.
        
        Returns:
            current signed value of the stepsize
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
        Get the number of evaluations of the differential equations function.
        
        The number of evaluations corresponds to the last call to the integrate method. It is 0 if the method has not been called yet.
        
        Returns:
            number of evaluations of the differential equations function
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.List[org.hipparchus.ode.events.FieldODEEventDetector[_FieldODEIntegrator__T]]:
        """
        Get all the event detectors that have been added to the integrator.
        
        Returns:
            an unmodifiable collection of the added events detectors
        
        Since:
            3.0
        
        Also see:
            addEventDetector,
            clearEventDetectors
        
        
        """
        ...
    def getMaxEvaluations(self) -> int:
        """
        Get the maximal number of functions evaluations.
        
        Returns:
            maximal number of functions evaluations
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the method.
        
        Returns:
            name of the method
        
        
        """
        ...
    def getStepEndHandlers(self) -> java.util.List[org.hipparchus.ode.events.FieldODEStepEndHandler[_FieldODEIntegrator__T]]:
        """
        Get all the handlers for step ends that have been added to the integrator.
        
        Returns:
            an unmodifiable list of the added step end handlers
        
        Since:
            3.0
        
        Also see:
            addStepEndHandler,
            clearStepEndHandlers
        
        
        """
        ...
    def getStepHandlers(self) -> java.util.List[org.hipparchus.ode.sampling.FieldODEStepHandler[_FieldODEIntegrator__T]]:
        """
        Get all the step handlers that have been added to the integrator.
        
        Returns:
            an unmodifiable collection of the added events handlers
        
        Also see:
            addStepHandler,
            clearStepHandlers
        
        
        """
        ...
    def getStepStart(self) -> 'FieldODEStateAndDerivative'[_FieldODEIntegrator__T]:
        """
        Get the state at step start time t :sub:`i` .
        
        This method can be called during integration (typically by the object implementing the FieldOrdinaryDifferentialEquation problem) if the value of the current step that is attempted is needed.
        
        The result is undefined if the method is called outside of calls to integrate.
        
        Returns:
            state at step start time t :sub:`i`
        
        
        """
        ...
    @typing.overload
    def integrate(self, equations: FieldExpandableODE[_FieldODEIntegrator__T], initialState: 'FieldODEState'[_FieldODEIntegrator__T], finalTime: _FieldODEIntegrator__T) -> 'FieldODEStateAndDerivative'[_FieldODEIntegrator__T]: ...
    @typing.overload
    def integrate(self, equations: 'FieldOrdinaryDifferentialEquation'[_FieldODEIntegrator__T], initialState: 'FieldODEState'[_FieldODEIntegrator__T], finalTime: _FieldODEIntegrator__T) -> 'FieldODEStateAndDerivative'[_FieldODEIntegrator__T]: ...
    def setMaxEvaluations(self, maxEvaluations: int) -> None:
        """
        Set the maximal number of differential equations function evaluations.
        
        The purpose of this method is to avoid infinite loops which can occur for example when stringent error constraints are set or when lots of discrete events are triggered, thus leading to many rejected steps.
        
        Parameters:
            maxEvaluations (int): maximal number of function evaluations (negative values are silently converted to maximal integer value, thus
                representing almost unlimited evaluations)
        
        
        """
        ...

_FieldODEState__T = typing.TypeVar('_FieldODEState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEState(typing.Generic[_FieldODEState__T]):
    """
    Container for time, main and secondary state vectors.
    
    Also see:
        FieldOrdinaryDifferentialEquation, FieldSecondaryODE,
        FieldODEIntegrator, FieldODEStateAndDerivative
    """
    @typing.overload
    def __init__(self, time: _FieldODEState__T, primaryState: typing.Union[typing.List[_FieldODEState__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, time: _FieldODEState__T, primaryState: typing.Union[typing.List[_FieldODEState__T], jpype.JArray], secondaryState: typing.Union[typing.List[typing.MutableSequence[_FieldODEState__T]], jpype.JArray]): ...
    def getCompleteState(self) -> typing.MutableSequence[_FieldODEState__T]:
        """
        Get complete state at time.
        
        Returns:
            complete state at time, starting with getPrimaryState, followed by all
            getSecondaryState in increasing index order
        
        Also see:
            getPrimaryState, getSecondaryState
        
        
        """
        ...
    def getCompleteStateDimension(self) -> int:
        """
        Return the dimension of the complete set of equations.
        
        The complete set of equations correspond to the primary set plus all secondary sets.
        
        Returns:
            dimension of the complete set of equations
        
        
        """
        ...
    def getNumberOfSecondaryStates(self) -> int:
        """
        Get the number of secondary states.
        
        Returns:
            number of secondary states.
        
        
        """
        ...
    def getPrimaryState(self) -> typing.MutableSequence[_FieldODEState__T]:
        """
        Get primary state at time.
        
        Returns:
            primary state at time
        
        Also see:
            getSecondaryState, getCompleteState
        
        
        """
        ...
    def getPrimaryStateDimension(self) -> int:
        """
        Get primary state dimension.
        
        Returns:
            primary state dimension
        
        Also see:
            getSecondaryStateDimension,
            getCompleteStateDimension
        
        
        """
        ...
    def getSecondaryState(self, index: int) -> typing.MutableSequence[_FieldODEState__T]:
        """
        Get secondary state at time.
        
        Parameters:
            index (int): index of the secondary set as returned by addSecondaryEquations (beware
                index 0 corresponds to primary state, secondary states start at 1)
        
        Returns:
            secondary state at time
        
        
        """
        ...
    def getSecondaryStateDimension(self, index: int) -> int:
        """
        Get secondary state dimension.
        
        Parameters:
            index (int): index of the secondary set as returned by addSecondaryEquations (beware
                index 0 corresponds to primary state, secondary states start at 1)
        
        Returns:
            secondary state dimension
        
        
        """
        ...
    def getTime(self) -> _FieldODEState__T:
        """
        Get time.
        
        Returns:
            time
        
        
        """
        ...

_FieldOrdinaryDifferentialEquation__T = typing.TypeVar('_FieldOrdinaryDifferentialEquation__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldOrdinaryDifferentialEquation(typing.Generic[_FieldOrdinaryDifferentialEquation__T]):
    """
    This interface represents a first order differential equations set.
    
    This interface should be implemented by all real first order differential equation problems before they can be handled by the integrators integrate method.
    
    A first order differential equations problem, as seen by an integrator is the time derivative dY/dt of a state vector Y, both being one dimensional arrays. From the integrator point of view, this derivative depends only on the current time t and on the state vector Y.
    
    For real problems, the derivative depends also on parameters that do not belong to the state vector (dynamical model constants for example). These constants are completely outside of the scope of this interface, the classes that implement it are allowed to handle them as they want.
    
    Also see:
        FieldODEIntegrator
    """
    def computeDerivatives(self, t: _FieldOrdinaryDifferentialEquation__T, y: typing.Union[typing.List[_FieldOrdinaryDifferentialEquation__T], jpype.JArray]) -> typing.MutableSequence[_FieldOrdinaryDifferentialEquation__T]:
        """
        Get the current time derivative of the state vector.
        
        Parameters:
            t (FieldOrdinaryDifferentialEquation): current value of the independent time variable
            y (FieldOrdinaryDifferentialEquation[]): array containing the current value of the state vector
        
        Returns:
            time derivative of the state vector
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the problem.
        
        Returns:
            dimension of the problem
        
        
        """
        ...
    def init(self, t0: _FieldOrdinaryDifferentialEquation__T, y0: typing.Union[typing.List[_FieldOrdinaryDifferentialEquation__T], jpype.JArray], finalTime: _FieldOrdinaryDifferentialEquation__T) -> None:
        """
        Initialize equations at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the equations to initialize some internal data if needed.
        
        The default implementation does nothing.
        
        Parameters:
            t0 (FieldOrdinaryDifferentialEquation): value of the independent time variable at integration start
            y0 (FieldOrdinaryDifferentialEquation[]): array containing the value of the state vector at integration start
            finalTime (FieldOrdinaryDifferentialEquation): target time for the integration
        
        
        """
        ...

_FieldSecondaryODE__T = typing.TypeVar('_FieldSecondaryODE__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldSecondaryODE(typing.Generic[_FieldSecondaryODE__T]):
    """
    This interface allows users to add secondary differential equations to a primary set of differential equations.
    
    In some cases users may need to integrate some problem-specific equations along with a primary set of differential equations. One example is optimal control where adjoined parameters linked to the minimized Hamiltonian must be integrated.
    
    This interface allows users to add such equations to a primary set of FieldOrdinaryDifferentialEquation thanks to the addSecondaryEquations method.
    
    Also see:
        FieldOrdinaryDifferentialEquation, FieldExpandableODE
    """
    def computeDerivatives(self, t: _FieldSecondaryODE__T, primary: typing.Union[typing.List[_FieldSecondaryODE__T], jpype.JArray], primaryDot: typing.Union[typing.List[_FieldSecondaryODE__T], jpype.JArray], secondary: typing.Union[typing.List[_FieldSecondaryODE__T], jpype.JArray]) -> typing.MutableSequence[_FieldSecondaryODE__T]:
        """
        Compute the derivatives related to the secondary state parameters.
        
        In some cases, additional equations can require to change the derivatives of the primary state (i.e. the content of the primaryDot array). One use case is optimal control, when the secondary equations handle co-state, which changes control, and the control changes the primary state. In this case, the primary and secondary equations are not really independent from each other, so if possible it would be better to put state and co-state and their equations all in the primary equations. As this is not always possible, this method explicitly allows to modify the content of the primaryDot array. This array will be used to evolve the primary state only after all secondary equations have computed their derivatives, hence allowing this side effect.
        
        Parameters:
            t (FieldSecondaryODE): current value of the independent time variable
            primary (FieldSecondaryODE[]): array containing the current value of the primary state vector
            primaryDot (FieldSecondaryODE[]): array containing the derivative of the primary state vector (the method is allowed to change the derivatives here, when
                the additional equations do have an effect on the primary equations)
            secondary (FieldSecondaryODE[]): array containing the current value of the secondary state vector
        
        Returns:
            derivative of the secondary state vector
        
        Raises:
            hipparchus: if the number of functions evaluations is exceeded
            hipparchus: if arrays dimensions do not match equations settings
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the secondary state parameters.
        
        Returns:
            dimension of the secondary state parameters
        
        
        """
        ...
    def init(self, t0: _FieldSecondaryODE__T, primary0: typing.Union[typing.List[_FieldSecondaryODE__T], jpype.JArray], secondary0: typing.Union[typing.List[_FieldSecondaryODE__T], jpype.JArray], finalTime: _FieldSecondaryODE__T) -> None:
        """
        Initialize equations at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the equations to initialize some internal data if needed.
        
        The default implementation does nothing.
        
        Parameters:
            t0 (FieldSecondaryODE): value of the independent time variable at integration start
            primary0 (FieldSecondaryODE[]): array containing the value of the primary state vector at integration start
            secondary0 (FieldSecondaryODE[]): array containing the value of the secondary state vector at integration start
            finalTime (FieldSecondaryODE): target time for the integration
        
        
        """
        ...

class LocalizedODEFormats(java.lang.Enum['LocalizedODEFormats'], org.hipparchus.exception.Localizable):
    """
    Enumeration for localized messages formats used in exceptions messages.
    
    The constants in this enumeration represent the available formats as localized strings. These formats are intended to be localized using simple properties files, using the constant name as the key and the property value as the message format. The source English format is provided in the constants themselves to serve both as a reminder for developers to understand the parameters needed by each format, as a basis for translators to create localized properties files, and as a default format if some translation is missing.
    """
    HOLE_BETWEEN_MODELS_TIME_RANGES: typing.ClassVar['LocalizedODEFormats'] = ...
    INTEGRATION_METHOD_NEEDS_AT_LEAST_TWO_PREVIOUS_POINTS: typing.ClassVar['LocalizedODEFormats'] = ...
    MINIMAL_STEPSIZE_REACHED_DURING_INTEGRATION: typing.ClassVar['LocalizedODEFormats'] = ...
    MULTISTEP_STARTER_STOPPED_EARLY: typing.ClassVar['LocalizedODEFormats'] = ...
    PROPAGATION_DIRECTION_MISMATCH: typing.ClassVar['LocalizedODEFormats'] = ...
    TOO_SMALL_INTEGRATION_INTERVAL: typing.ClassVar['LocalizedODEFormats'] = ...
    UNKNOWN_PARAMETER: typing.ClassVar['LocalizedODEFormats'] = ...
    UNMATCHED_ODE_IN_EXPANDED_SET: typing.ClassVar['LocalizedODEFormats'] = ...
    NAN_APPEARING_DURING_INTEGRATION: typing.ClassVar['LocalizedODEFormats'] = ...
    FIND_ROOT: typing.ClassVar['LocalizedODEFormats'] = ...
    @typing.overload
    def getLocalizedString(self, string: str, string2: str, locale: java.util.Locale) -> str: ...
    @typing.overload
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
        Specified by: hipparchus in interface hipparchus
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
        Specified by: hipparchus in interface hipparchus
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'LocalizedODEFormats':
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
    def values() -> typing.MutableSequence['LocalizedODEFormats']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (LocalizedODEFormats c : LocalizedODEFormats.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_MultistepFieldIntegrator__T = typing.TypeVar('_MultistepFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class MultistepFieldIntegrator(org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator[_MultistepFieldIntegrator__T], typing.Generic[_MultistepFieldIntegrator__T]):
    """
    This class is the base class for multistep integrators for Ordinary Differential Equations.
    
    We define scaled derivatives s :sub:`i` (n) at step n as: \[ \left\{\begin{align} s_1(n) &= h y'_n \text{ for first derivative}\\ s_2(n) &= \frac{h^2}{2} y_n'' \text{ for second derivative}\\ s_3(n) &= \frac{h^3}{6} y_n''' \text{ for third derivative}\\ &\cdots\\ s_k(n) &= \frac{h^k}{k!} y_n^{(k)} \text{ for } k^\mathrm{th} \text{ derivative} \end{align}\right. \]
    
    Rather than storing several previous steps separately, this implementation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same step (y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as: \[ r_n = [ s_2(n), s_3(n) \ldots s_k(n) ]^T \] (we omit the k index in the notation for clarity)
    
    Multistep integrators with Nordsieck representation are highly sensitive to large step changes because when the step is multiplied by factor a, the k :sup:`th` component of the Nordsieck vector is multiplied by a :sup:`k` and the last components are the least accurate ones. The default max growth factor is therefore set to a quite low value: 2 :sup:`1/order` .
    
    Also see:
        AdamsBashforthFieldIntegrator,
        AdamsMoultonFieldIntegrator
    """
    def getMaxGrowth(self) -> float:
        """
        Get the maximal growth factor for stepsize control.
        
        Returns:
            maximal growth factor
        
        
        """
        ...
    def getMinReduction(self) -> float:
        """
        Get the minimal reduction factor for stepsize control.
        
        Returns:
            minimal reduction factor
        
        
        """
        ...
    def getNSteps(self) -> int:
        """
        Get the number of steps of the multistep method (excluding the one being computed).
        
        Returns:
            number of steps of the multistep method (excluding the one being computed)
        
        
        """
        ...
    def getSafety(self) -> float:
        """
        Get the safety factor for stepsize control.
        
        Returns:
            safety factor
        
        
        """
        ...
    def getStarterIntegrator(self) -> FieldODEIntegrator[_MultistepFieldIntegrator__T]:
        """
        Get the starter integrator.
        
        Returns:
            starter integrator
        
        
        """
        ...
    def setMaxGrowth(self, maxGrowth: float) -> None:
        """
        Set the maximal growth factor for stepsize control.
        
        Parameters:
            maxGrowth (double): maximal growth factor
        
        
        """
        ...
    def setMinReduction(self, minReduction: float) -> None:
        """
        Set the minimal reduction factor for stepsize control.
        
        Parameters:
            minReduction (double): minimal reduction factor
        
        
        """
        ...
    def setSafety(self, safety: float) -> None:
        """
        Set the safety factor for stepsize control.
        
        Parameters:
            safety (double): safety factor
        
        
        """
        ...
    def setStarterIntegrator(self, starterIntegrator: FieldODEIntegrator[_MultistepFieldIntegrator__T]) -> None:
        """
        Set the starter integrator.
        
        The various step and event handlers for this starter integrator will be managed automatically by the multi-step integrator. Any user configuration for these elements will be cleared before use.
        
        Parameters:
            starterIntegrator (FieldODEIntegrator<MultistepFieldIntegrator> starterIntegrator): starter integrator
        
        
        """
        ...

class MultistepIntegrator(org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator):
    """
    This class is the base class for multistep integrators for Ordinary Differential Equations.
    
    We define scaled derivatives s :sub:`i` (n) at step n as: \[ \left\{\begin{align} s_1(n) &= h y'_n \text{ for first derivative}\\ s_2(n) &= \frac{h^2}{2} y_n'' \text{ for second derivative}\\ s_3(n) &= \frac{h^3}{6} y_n''' \text{ for third derivative}\\ &\cdots\\ s_k(n) &= \frac{h^k}{k!} y_n^{(k)} \text{ for } k^\mathrm{th} \text{ derivative} \end{align}\right. \]
    
    Rather than storing several previous steps separately, this implementation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same step (y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as: \[ r_n = [ s_2(n), s_3(n) \ldots s_k(n) ]^T \] (we omit the k index in the notation for clarity)
    
    Multistep integrators with Nordsieck representation are highly sensitive to large step changes because when the step is multiplied by factor a, the k :sup:`th` component of the Nordsieck vector is multiplied by a :sup:`k` and the last components are the least accurate ones. The default max growth factor is therefore set to a quite low value: 2 :sup:`1/order` .
    
    Also see:
        AdamsBashforthIntegrator,
        AdamsMoultonIntegrator
    """
    def getMaxGrowth(self) -> float:
        """
        Get the maximal growth factor for stepsize control.
        
        Returns:
            maximal growth factor
        
        
        """
        ...
    def getMinReduction(self) -> float:
        """
        Get the minimal reduction factor for stepsize control.
        
        Returns:
            minimal reduction factor
        
        
        """
        ...
    def getNSteps(self) -> int:
        """
        Get the number of steps of the multistep method (excluding the one being computed).
        
        Returns:
            number of steps of the multistep method (excluding the one being computed)
        
        
        """
        ...
    def getSafety(self) -> float:
        """
        Get the safety factor for stepsize control.
        
        Returns:
            safety factor
        
        
        """
        ...
    def getStarterIntegrator(self) -> 'ODEIntegrator':
        """
        Get the starter integrator.
        
        Returns:
            starter integrator
        
        
        """
        ...
    def setMaxGrowth(self, maxGrowth: float) -> None:
        """
        Set the maximal growth factor for stepsize control.
        
        Parameters:
            maxGrowth (double): maximal growth factor
        
        
        """
        ...
    def setMinReduction(self, minReduction: float) -> None:
        """
        Set the minimal reduction factor for stepsize control.
        
        Parameters:
            minReduction (double): minimal reduction factor
        
        
        """
        ...
    def setSafety(self, safety: float) -> None:
        """
        Set the safety factor for stepsize control.
        
        Parameters:
            safety (double): safety factor
        
        
        """
        ...
    def setStarterIntegrator(self, starterIntegrator: 'ODEIntegrator') -> None:
        """
        Set the starter integrator.
        
        The various step and event handlers for this starter integrator will be managed automatically by the multi-step integrator. Any user configuration for these elements will be cleared before use.
        
        Parameters:
            starterIntegrator (ODEIntegrator): starter integrator
        
        
        """
        ...

class ODEIntegrator:
    """
    This interface represents a first order integrator for differential equations.
    
    The classes which are devoted to solve first order differential equations should implement this interface. The problems which can be handled should implement the OrdinaryDifferentialEquation interface.
    
    Also see:
        OrdinaryDifferentialEquation, ODEStepHandler,
        ODEEventHandler
    """
    def addEventDetector(self, detector: org.hipparchus.ode.events.ODEEventDetector) -> None:
        """
        Add an event detector to the integrator.
        
        Parameters:
            detector (ODEEventDetector): event detector
        
        Since:
            3.0
        
        Also see:
            getEventDetectors,
            clearEventDetectors
        
        
        """
        ...
    def addStepEndHandler(self, handler: typing.Union[org.hipparchus.ode.events.ODEStepEndHandler, typing.Callable]) -> None:
        """
        Add a handler for step ends to the integrator.
        
        The stepEndOccurred method of the handler will be called at each step end.
        
        Parameters:
            handler (ODEStepEndHandler): handler for step ends
        
        Since:
            3.0
        
        Also see:
            getStepEndHandlers,
            clearStepEndHandlers
        
        
        """
        ...
    def addStepHandler(self, handler: typing.Union[org.hipparchus.ode.sampling.ODEStepHandler, typing.Callable]) -> None:
        """
        Add a step handler to this integrator.
        
        The handler will be called by the integrator for each accepted step.
        
        Parameters:
            handler (ODEStepHandler): handler for the accepted steps
        
        Also see:
            getStepHandlers, clearStepHandlers
        
        
        """
        ...
    def clearEventDetectors(self) -> None:
        """
        Remove all the event handlers that have been added to the integrator.
        
        Since:
            3.0
        
        Also see:
            addEventDetector, getEventDetectors
        
        
        """
        ...
    def clearStepEndHandlers(self) -> None:
        """
        Remove all the handlers for step ends that have been added to the integrator.
        
        Since:
            3.0
        
        Also see:
            addStepEndHandler,
            getStepEndHandlers
        
        
        """
        ...
    def clearStepHandlers(self) -> None:
        """
        Remove all the step handlers that have been added to the integrator.
        
        Also see:
            addStepHandler, getStepHandlers
        
        
        """
        ...
    def getCurrentSignedStepsize(self) -> float:
        """
        Get the current signed value of the integration stepsize.
        
        This method can be called during integration (typically by the object implementing the OrdinaryDifferentialEquation problem) if the signed value of the current stepsize that is tried is needed.
        
        The result is undefined if the method is called outside of calls to integrate.
        
        Returns:
            current signed value of the stepsize
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
        Get the number of evaluations of the differential equations function.
        
        The number of evaluations corresponds to the last call to the integrate method. It is 0 if the method has not been called yet.
        
        Returns:
            number of evaluations of the differential equations function
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.List[org.hipparchus.ode.events.ODEEventDetector]:
        """
        Get all the event detectors that have been added to the integrator.
        
        Returns:
            an unmodifiable list of the added events detectors
        
        Since:
            3.0
        
        Also see:
            addEventDetector,
            clearEventDetectors
        
        
        """
        ...
    def getMaxEvaluations(self) -> int:
        """
        Get the maximal number of functions evaluations.
        
        Returns:
            maximal number of functions evaluations
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the method.
        
        Returns:
            name of the method
        
        
        """
        ...
    def getStepEndHandlers(self) -> java.util.List[org.hipparchus.ode.events.ODEStepEndHandler]:
        """
        Get all the handlers for step ends that have been added to the integrator.
        
        Returns:
            an unmodifiable list of the added step end handlers
        
        Since:
            3.0
        
        Also see:
            addStepEndHandler,
            clearStepEndHandlers
        
        
        """
        ...
    def getStepHandlers(self) -> java.util.List[org.hipparchus.ode.sampling.ODEStepHandler]:
        """
        Get all the step handlers that have been added to the integrator.
        
        Returns:
            an unmodifiable collection of the added events handlers
        
        Also see:
            addStepHandler, clearStepHandlers
        
        
        """
        ...
    def getStepStart(self) -> 'ODEStateAndDerivative':
        """
        Get the state at step start time t :sub:`i` .
        
        This method can be called during integration (typically by the object implementing the OrdinaryDifferentialEquation problem) if the value of the current step that is attempted is needed.
        
        The result is undefined if the method is called outside of calls to integrate.
        
        Returns:
            state at step start time t :sub:`i`
        
        
        """
        ...
    @typing.overload
    def integrate(self, equations: ExpandableODE, initialState: 'ODEState', finalTime: float) -> 'ODEStateAndDerivative': ...
    @typing.overload
    def integrate(self, equations: 'OrdinaryDifferentialEquation', initialState: 'ODEState', finalTime: float) -> 'ODEStateAndDerivative': ...
    def setMaxEvaluations(self, maxEvaluations: int) -> None:
        """
        Set the maximal number of differential equations function evaluations.
        
        The purpose of this method is to avoid infinite loops which can occur for example when stringent error constraints are set or when lots of discrete events are triggered, thus leading to many rejected steps.
        
        Parameters:
            maxEvaluations (int): maximal number of function evaluations (negative values are silently converted to maximal integer value, thus
                representing almost unlimited evaluations)
        
        
        """
        ...

class ODEState(java.io.Serializable):
    """
    Container for time, main and secondary state vectors.
    
    Also see:
        OrdinaryDifferentialEquation, SecondaryODE,
        ODEIntegrator, ODEStateAndDerivative, serialized
    """
    @typing.overload
    def __init__(self, time: float, primaryState: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, time: float, primaryState: typing.Union[typing.List[float], jpype.JArray], secondaryState: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    def getCompleteState(self) -> typing.MutableSequence[float]:
        """
        Get complete state at time.
        
        Returns:
            complete state at time, starting with getPrimaryState, followed by all
            getSecondaryState in increasing index order
        
        Also see:
            getPrimaryState, getSecondaryState
        
        
        """
        ...
    def getCompleteStateDimension(self) -> int:
        """
        Return the dimension of the complete set of equations.
        
        The complete set of equations correspond to the primary set plus all secondary sets.
        
        Returns:
            dimension of the complete set of equations
        
        Also see:
            getPrimaryStateDimension,
            getSecondaryStateDimension
        
        
        """
        ...
    def getNumberOfSecondaryStates(self) -> int:
        """
        Get the number of secondary states.
        
        Returns:
            number of secondary states.
        
        
        """
        ...
    def getPrimaryState(self) -> typing.MutableSequence[float]:
        """
        Get primary state at time.
        
        Returns:
            primary state at time
        
        Also see:
            getSecondaryState, getCompleteState
        
        
        """
        ...
    def getPrimaryStateDimension(self) -> int:
        """
        Get primary state dimension.
        
        Returns:
            primary state dimension
        
        Also see:
            getSecondaryStateDimension,
            getCompleteStateDimension
        
        
        """
        ...
    def getSecondaryState(self, index: int) -> typing.MutableSequence[float]:
        """
        Get secondary state at time.
        
        Parameters:
            index (int): index of the secondary set as returned by addSecondaryEquations (beware index
                0 corresponds to primary state, secondary states start at 1)
        
        Returns:
            secondary state at time
        
        Also see:
            getPrimaryState, getCompleteState
        
        
        """
        ...
    def getSecondaryStateDimension(self, index: int) -> int:
        """
        Get secondary state dimension.
        
        Parameters:
            index (int): index of the secondary set as returned by addSecondaryEquations (beware index
                0 corresponds to primary state, secondary states start at 1)
        
        Returns:
            secondary state dimension
        
        Also see:
            getPrimaryStateDimension,
            getCompleteStateDimension
        
        
        """
        ...
    def getTime(self) -> float:
        """
        Get time.
        
        Returns:
            time
        
        
        """
        ...

class OrdinaryDifferentialEquation:
    """
    This interface represents a first order differential equations set.
    
    This interface should be implemented by all real first order differential equation problems before they can be handled by the integrators integrate method.
    
    A first order differential equations problem, as seen by an integrator is the time derivative dY/dt of a state vector Y, both being one dimensional arrays. From the integrator point of view, this derivative depends only on the current time t and on the state vector Y.
    
    For real problems, the derivative depends also on parameters that do not belong to the state vector (dynamical model constants for example). These constants are completely outside of the scope of this interface, the classes that implement it are allowed to handle them as they want.
    
    Also see:
        ODEIntegrator, FirstOrderConverter,
        SecondOrderODE
    """
    def computeDerivatives(self, t: float, y: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Get the current time derivative of the state vector.
        
        Parameters:
            t (double): current value of the independent time variable
            y (double[]): array containing the current value of the state vector
        
        Returns:
            time derivative of the state vector
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the problem.
        
        Returns:
            dimension of the problem
        
        
        """
        ...
    def init(self, t0: float, y0: typing.Union[typing.List[float], jpype.JArray], finalTime: float) -> None:
        """
        Initialize equations at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the equations to initialize some internal data if needed.
        
        The default implementation does nothing.
        
        Parameters:
            t0 (double): value of the independent time variable at integration start
            y0 (double[]): array containing the value of the state vector at integration start
            finalTime (double): target time for the integration
        
        
        """
        ...

class ParameterConfiguration:
    """
    Simple container pairing a parameter name with a step in order to compute the associated Jacobian matrix by finite difference.
    
    Instances of this class are guaranteed to be immutable.
    """
    def getHP(self) -> float:
        """
        Get parameter step.
        
        Returns:
            parameter step
        
        
        """
        ...
    def getParameterName(self) -> str:
        """
        Get parameter name.
        
        Returns:
            parameter name
        
        
        """
        ...

class Parameterizable:
    """
    This interface enables to process any parameterizable object.
    """
    def getParametersNames(self) -> java.util.List[str]:
        """
        Get the names of the supported parameters.
        
        Returns:
            parameters names
        
        Also see:
            isSupported
        
        
        """
        ...
    def isSupported(self, name: str) -> bool:
        """
        Check if a parameter is supported.
        
        Supported parameters are those listed by getParametersNames.
        
        Parameters:
            name (String): parameter name to check
        
        Returns:
            true if the parameter is supported
        
        Also see:
            getParametersNames
        
        
        """
        ...

class SecondOrderODE:
    """
    This interface represents a second order differential equations set.
    
    This interface should be implemented by all real second order differential equation problems before they can be handled by the integrators FirstOrderConverter.
    
    A second order differential equations problem, as seen by an integrator is the second time derivative d2Y/dt^2 of a state vector Y, both being one dimensional arrays. From the integrator point of view, this derivative depends only on the current time t, on the state vector Y and on the first time derivative of the state vector.
    
    For real problems, the derivative depends also on parameters that do not belong to the state vector (dynamical model constants for example). These constants are completely outside of the scope of this interface, the classes that implement it are allowed to handle them as they want.
    
    Also see:
        FirstOrderConverter, OrdinaryDifferentialEquation
    """
    def computeSecondDerivatives(self, t: float, y: typing.Union[typing.List[float], jpype.JArray], yDot: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Get the current time derivative of the state vector.
        
        Parameters:
            t (double): current value of the independent time variable
            y (double[]): array containing the current value of the state vector
            yDot (double[]): array containing the current value of the first derivative of the state vector
        
        Returns:
            second time derivative of the state vector
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the problem.
        
        Returns:
            dimension of the problem
        
        
        """
        ...

class SecondaryODE:
    """
    This interface allows users to add secondary differential equations to a primary set of differential equations.
    
    In some cases users may need to integrate some problem-specific equations along with a primary set of differential equations. One example is optimal control where adjoined parameters linked to the minimized hamiltonian must be integrated.
    
    This interface allows users to add such equations to a primary set of OrdinaryDifferentialEquation thanks to the addSecondaryEquations method.
    
    Also see:
        ExpandableODE
    """
    def computeDerivatives(self, t: float, primary: typing.Union[typing.List[float], jpype.JArray], primaryDot: typing.Union[typing.List[float], jpype.JArray], secondary: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Compute the derivatives related to the secondary state parameters.
        
        In some cases, additional equations can require to change the derivatives of the primary state (i.e. the content of the primaryDot array). One use case is optimal control, when the secondary equations handle co-state, which changes control, and the control changes the primary state. In this case, the primary and secondary equations are not really independent from each other, so if possible it would be better to put state and co-state and their equations all in the primary equations. As this is not always possible, this method explicitly allows to modify the content of the primaryDot array. This array will be used to evolve the primary state only after all secondary equations have computed their derivatives, hence allowing this side effect.
        
        Parameters:
            t (double): current value of the independent time variable
            primary (double[]): array containing the current value of the primary state vector
            primaryDot (double[]): array containing the derivative of the primary state vector (the method is allowed to change the derivatives here, when
                the additional equations do have an effect on the primary equations)
            secondary (double[]): array containing the current value of the secondary state vector
        
        Returns:
            derivative of the secondary state vector
        
        Raises:
            hipparchus: if the number of functions evaluations is exceeded
            hipparchus: if arrays dimensions do not match equations settings
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the secondary state parameters.
        
        Returns:
            dimension of the secondary state parameters
        
        
        """
        ...
    def init(self, t0: float, primary0: typing.Union[typing.List[float], jpype.JArray], secondary0: typing.Union[typing.List[float], jpype.JArray], finalTime: float) -> None:
        """
        Initialize equations at the start of an ODE integration.
        
        This method is called once at the start of the integration. It may be used by the equations to initialize some internal data if needed.
        
        The default implementation does nothing.
        
        Parameters:
            t0 (double): value of the independent time variable at integration start
            primary0 (double[]): array containing the value of the primary state vector at integration start
            secondary0 (double[]): array containing the value of the secondary state vector at integration start
            finalTime (double): target time for the integration
        
        
        """
        ...

class VariationalEquation:
    """
    This class defines a set of SecondaryODE to compute the global Jacobian matrices with respect to the initial state vector and, if any, to some parameters of the primary ODE set.
    
    The primary set of ODE for which Jaobian matrices are requested may be:
    
      - a full-fledged ODEJacobiansProvider that computes by itself both the ODE and its local
        partial derivatives,
      - a simple OrdinaryDifferentialEquation which must therefore be completed with a finite
        differences configuration to compute local partial derivatives (so-called internal differentiation).
    
    As the variational equation automatically inserts addSecondaryEquations, in the ExpandableODE, data for initial state must also be inserted before integration and matrices result must be extracted after integration. This implies a precise scheduling of the calls to the various methods of this class. The proper scheduling is the following one:
    
    
       // set up equations
       ODEJacobiansProvider jode       = new MyODE(...);
       ExpandableODE        expandable = new Expandable(jode);
       VariationalEquation  ve         = new VariationalEquation(expandable, jode);
    
       // set up initial state
       ODEState initWithoutDerivatives = new ODEState(t0, y0);
       ve.setInitialMainStateJacobian(dYdY0); // only needed if the default identity matrix is not suitable
       ve.setInitialParameterJacobian(name, dYdP); // only needed if the default zero matrix is not suitable
       ODEState initWithDerivatives = ve.setUpInitialState(initWithoutDerivatives);
    
       // perform integration on the expanded equations with the expanded initial state
       ODEStateAndDerivative finalState = integrator.integrate(expandable, initWithDerivatives, finalT);
    
       // extract Jacobian matrices
       dYdY0 = ve.extractMainSetJacobian(finalState);
       dYdP  = ve.extractParameterJacobian(finalState, name);
     
    
    The most important part is to not forget to call setUpInitialState to add the secondary state with the initial matrices to the ODEState used in the integrate method. Forgetting to do this and passing only a ODEState without the secondary state set up will trigger an error as the state vector will not have the correct dimension.
    
    Also see:
        ExpandableODE, ODEJacobiansProvider,
        OrdinaryDifferentialEquation, NamedParameterJacobianProvider,
        ParametersController
    """
    @typing.overload
    def __init__(self, expandable: ExpandableODE, jode: 'ODEJacobiansProvider'): ...
    @typing.overload
    def __init__(self, expandable: ExpandableODE, ode: OrdinaryDifferentialEquation, hY: typing.Union[typing.List[float], jpype.JArray], controller: 'ParametersController', *paramsAndSteps: ParameterConfiguration): ...
    def extractMainSetJacobian(self, state: ODEState) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Extract the Jacobian matrix with respect to state.
        
        Parameters:
            state (ODEState): state from which to extract Jacobian matrix
        
        Returns:
            Jacobian matrix dY/dY0 with respect to state.
        
        
        """
        ...
    def extractParameterJacobian(self, state: ODEState, pName: str) -> typing.MutableSequence[float]:
        """
        Extract the Jacobian matrix with respect to one parameter.
        
        Parameters:
            state (ODEState): state from which to extract Jacobian matrix
            pName (String): name of the parameter for the computed Jacobian matrix
        
        Returns:
            Jacobian matrix dY/dP with respect to the named parameter
        
        
        """
        ...
    def setInitialMainStateJacobian(self, dYdY0: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
        Set the initial value of the Jacobian matrix with respect to state.
        
        If this method is not called, the initial value of the Jacobian matrix with respect to state is set to identity.
        
        This method must be called before setUpInitialState
        
        Parameters:
            dYdY0 (double[][]): initial Jacobian matrix w.r.t. state
        
        Raises:
            hipparchus: if matrix dimensions are incorrect
        
        
        """
        ...
    def setInitialParameterJacobian(self, pName: str, dYdP: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set the initial value of a column of the Jacobian matrix with respect to one parameter.
        
        If this method is not called for some parameter, the initial value of the column of the Jacobian matrix with respect to this parameter is set to zero.
        
        This method must be called before setUpInitialState
        
        Parameters:
            pName (String): parameter name
            dYdP (double[]): initial Jacobian column vector with respect to the parameter
        
        Raises:
            hipparchus: if a parameter is not supported
            hipparchus: if the column vector does not match state dimension
        
        
        """
        ...
    def setUpInitialState(self, initialState: ODEState) -> ODEState:
        """
        Set up initial state.
        
        This method inserts the initial Jacobian matrices data into an ODEState by overriding the additional state components corresponding to the instance. It must be called prior to integrate the equations.
        
        This method must be called after setInitialMainStateJacobian and setInitialParameterJacobian.
        
        Parameters:
            initialState (ODEState): initial state, without the initial Jacobians matrices
        
        Returns:
            a new instance of initial state, with the initial Jacobians matrices properly initialized
        
        
        """
        ...
    class MismatchedEquations(org.hipparchus.exception.MathIllegalArgumentException):
        def __init__(self): ...

_AbstractFieldIntegrator__T = typing.TypeVar('_AbstractFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AbstractFieldIntegrator(FieldODEIntegrator[_AbstractFieldIntegrator__T], typing.Generic[_AbstractFieldIntegrator__T]):
    """
    Base class managing common boilerplate for all integrators.
    """
    def addEventDetector(self, detector: org.hipparchus.ode.events.FieldODEEventDetector[_AbstractFieldIntegrator__T]) -> None:
        """
        Add an event detector to the integrator.
        
        Specified by: addEventDetector in interface FieldODEIntegrator
        
        Parameters:
            detector (FieldODEEventDetector<AbstractFieldIntegrator> detector): event detector
        
        Also see:
            getEventDetectors,
            clearEventDetectors
        
        
        """
        ...
    def addStepEndHandler(self, handler: typing.Union[org.hipparchus.ode.events.FieldODEStepEndHandler[_AbstractFieldIntegrator__T], typing.Callable[['FieldODEStateAndDerivative'[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]]) -> None:
        """
        Add a handler for step ends to the integrator.
        
        The stepEndOccurred method of the handler will be called at each step end.
        
        Specified by: addStepEndHandler in interface FieldODEIntegrator
        
        Parameters:
            handler (FieldODEStepEndHandler<AbstractFieldIntegrator> handler): handler for step ends
        
        Also see:
            getStepEndHandlers,
            clearStepEndHandlers
        
        
        """
        ...
    def addStepHandler(self, handler: typing.Union[org.hipparchus.ode.sampling.FieldODEStepHandler[_AbstractFieldIntegrator__T], typing.Callable[[org.hipparchus.ode.sampling.FieldODEStateInterpolator[org.hipparchus.CalculusFieldElement]], None]]) -> None:
        """
        Add a step handler to this integrator.
        
        The handler will be called by the integrator for each accepted step.
        
        Specified by: addStepHandler in interface FieldODEIntegrator
        
        Parameters:
            handler (FieldODEStepHandler<AbstractFieldIntegrator> handler): handler for the accepted steps
        
        Also see:
            getStepHandlers,
            clearStepHandlers
        
        
        """
        ...
    def clearEventDetectors(self) -> None:
        """
        Remove all the event handlers that have been added to the integrator.
        
        Specified by: clearEventDetectors in interface FieldODEIntegrator
        
        Also see:
            addEventDetector,
            getEventDetectors
        
        
        """
        ...
    def clearStepEndHandlers(self) -> None:
        """
        Remove all the handlers for step ends that have been added to the integrator.
        
        Specified by: clearStepEndHandlers in interface FieldODEIntegrator
        
        Also see:
            addStepEndHandler,
            getStepEndHandlers
        
        
        """
        ...
    def clearStepHandlers(self) -> None:
        """
        Remove all the step handlers that have been added to the integrator.
        
        Specified by: clearStepHandlers in interface FieldODEIntegrator
        
        Also see:
            addStepHandler,
            getStepHandlers
        
        
        """
        ...
    def computeDerivatives(self, t: _AbstractFieldIntegrator__T, y: typing.Union[typing.List[_AbstractFieldIntegrator__T], jpype.JArray]) -> typing.MutableSequence[_AbstractFieldIntegrator__T]:
        """
        Compute the derivatives and check the number of evaluations.
        
        Parameters:
            t (AbstractFieldIntegrator): current value of the independent time variable
            y (AbstractFieldIntegrator[]): array containing the current value of the state vector
        
        Returns:
            state completed with derivatives
        
        Raises:
            hipparchus: if arrays dimensions do not match equations settings
            hipparchus: if the number of functions evaluations is exceeded
            NullPointerException: if the ODE equations have not been set (i.e. if this method is called outside of a call to
                integrate
        
        
        """
        ...
    def getCurrentSignedStepsize(self) -> _AbstractFieldIntegrator__T:
        """
        Get the current signed value of the integration stepsize.
        
        This method can be called during integration (typically by the object implementing the FieldOrdinaryDifferentialEquation problem) if the signed value of the current stepsize that is tried is needed.
        
        The result is undefined if the method is called outside of calls to integrate.
        
        Specified by: getCurrentSignedStepsize in interface FieldODEIntegrator
        
        Returns:
            current signed value of the stepsize
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
        Get the number of evaluations of the differential equations function.
        
        The number of evaluations corresponds to the last call to the integrate method. It is 0 if the method has not been called yet.
        
        Specified by: getEvaluations in interface FieldODEIntegrator
        
        Returns:
            number of evaluations of the differential equations function
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.List[org.hipparchus.ode.events.FieldODEEventDetector[_AbstractFieldIntegrator__T]]:
        """
        Get all the event detectors that have been added to the integrator.
        
        Specified by: getEventDetectors in interface FieldODEIntegrator
        
        Returns:
            an unmodifiable collection of the added events detectors
        
        Also see:
            addEventDetector,
            clearEventDetectors
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_AbstractFieldIntegrator__T]:
        """
        Get the field to which state vector elements belong.
        
        Returns:
            field to which state vector elements belong
        
        
        """
        ...
    def getMaxEvaluations(self) -> int:
        """
        Get the maximal number of functions evaluations.
        
        Specified by: getMaxEvaluations in interface FieldODEIntegrator
        
        Returns:
            maximal number of functions evaluations
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the method.
        
        Specified by: getName in interface FieldODEIntegrator
        
        Returns:
            name of the method
        
        
        """
        ...
    def getStepEndHandlers(self) -> java.util.List[org.hipparchus.ode.events.FieldODEStepEndHandler[_AbstractFieldIntegrator__T]]:
        """
        Get all the handlers for step ends that have been added to the integrator.
        
        Specified by: getStepEndHandlers in interface FieldODEIntegrator
        
        Returns:
            an unmodifiable list of the added step end handlers
        
        Also see:
            addStepEndHandler,
            clearStepEndHandlers
        
        
        """
        ...
    def getStepHandlers(self) -> java.util.List[org.hipparchus.ode.sampling.FieldODEStepHandler[_AbstractFieldIntegrator__T]]:
        """
        Get all the step handlers that have been added to the integrator.
        
        Specified by: getStepHandlers in interface FieldODEIntegrator
        
        Returns:
            an unmodifiable collection of the added events handlers
        
        Also see:
            addStepHandler,
            clearStepHandlers
        
        
        """
        ...
    def getStepStart(self) -> 'FieldODEStateAndDerivative'[_AbstractFieldIntegrator__T]:
        """
        Get the state at step start time t :sub:`i` .
        
        This method can be called during integration (typically by the object implementing the FieldOrdinaryDifferentialEquation problem) if the value of the current step that is attempted is needed.
        
        The result is undefined if the method is called outside of calls to integrate.
        
        Specified by: getStepStart in interface FieldODEIntegrator
        
        Returns:
            state at step start time t :sub:`i`
        
        
        """
        ...
    def setMaxEvaluations(self, maxEvaluations: int) -> None:
        """
        Set the maximal number of differential equations function evaluations.
        
        The purpose of this method is to avoid infinite loops which can occur for example when stringent error constraints are set or when lots of discrete events are triggered, thus leading to many rejected steps.
        
        Specified by: setMaxEvaluations in interface FieldODEIntegrator
        
        Parameters:
            maxEvaluations (int): maximal number of function evaluations (negative values are silently converted to maximal integer value, thus
                representing almost unlimited evaluations)
        
        
        """
        ...

class AbstractIntegrator(ODEIntegrator):
    """
    Base class managing common boilerplate for all integrators.
    """
    def addEventDetector(self, detector: org.hipparchus.ode.events.ODEEventDetector) -> None:
        """
        Add an event detector to the integrator.
        
        Specified by: addEventDetector in interface ODEIntegrator
        
        Parameters:
            detector (ODEEventDetector): event detector
        
        Also see:
            getEventDetectors,
            clearEventDetectors
        
        
        """
        ...
    def addStepEndHandler(self, handler: typing.Union[org.hipparchus.ode.events.ODEStepEndHandler, typing.Callable]) -> None:
        """
        Add a handler for step ends to the integrator.
        
        The stepEndOccurred method of the handler will be called at each step end.
        
        Specified by: addStepEndHandler in interface ODEIntegrator
        
        Parameters:
            handler (ODEStepEndHandler): handler for step ends
        
        Also see:
            getStepEndHandlers,
            clearStepEndHandlers
        
        
        """
        ...
    def addStepHandler(self, handler: typing.Union[org.hipparchus.ode.sampling.ODEStepHandler, typing.Callable]) -> None:
        """
        Add a step handler to this integrator.
        
        The handler will be called by the integrator for each accepted step.
        
        Specified by: addStepHandler in interface ODEIntegrator
        
        Parameters:
            handler (ODEStepHandler): handler for the accepted steps
        
        Also see:
            getStepHandlers, clearStepHandlers
        
        
        """
        ...
    def clearEventDetectors(self) -> None:
        """
        Remove all the event handlers that have been added to the integrator.
        
        Specified by: clearEventDetectors in interface ODEIntegrator
        
        Also see:
            addEventDetector, getEventDetectors
        
        
        """
        ...
    def clearStepEndHandlers(self) -> None:
        """
        Remove all the handlers for step ends that have been added to the integrator.
        
        Specified by: clearStepEndHandlers in interface ODEIntegrator
        
        Also see:
            addStepEndHandler,
            getStepEndHandlers
        
        
        """
        ...
    def clearStepHandlers(self) -> None:
        """
        Remove all the step handlers that have been added to the integrator.
        
        Specified by: clearStepHandlers in interface ODEIntegrator
        
        Also see:
            addStepHandler, getStepHandlers
        
        
        """
        ...
    def computeDerivatives(self, t: float, y: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Compute the derivatives and check the number of evaluations.
        
        Parameters:
            t (double): current value of the independent time variable
            y (double[]): array containing the current value of the state vector
        
        Returns:
            state completed with derivatives
        
        Raises:
            hipparchus: if arrays dimensions do not match equations settings
            hipparchus: if the number of functions evaluations is exceeded
            NullPointerException: if the ODE equations have not been set (i.e. if this method is called outside of a call to
                integrate
        
        
        """
        ...
    def getCurrentSignedStepsize(self) -> float:
        """
        Get the current signed value of the integration stepsize.
        
        This method can be called during integration (typically by the object implementing the OrdinaryDifferentialEquation problem) if the signed value of the current stepsize that is tried is needed.
        
        The result is undefined if the method is called outside of calls to integrate.
        
        Specified by: getCurrentSignedStepsize in interface ODEIntegrator
        
        Returns:
            current signed value of the stepsize
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
        Get the number of evaluations of the differential equations function.
        
        The number of evaluations corresponds to the last call to the integrate method. It is 0 if the method has not been called yet.
        
        Specified by: getEvaluations in interface ODEIntegrator
        
        Returns:
            number of evaluations of the differential equations function
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.List[org.hipparchus.ode.events.ODEEventDetector]:
        """
        Get all the event detectors that have been added to the integrator.
        
        Specified by: getEventDetectors in interface ODEIntegrator
        
        Returns:
            an unmodifiable list of the added events detectors
        
        Also see:
            addEventDetector,
            clearEventDetectors
        
        
        """
        ...
    def getMaxEvaluations(self) -> int:
        """
        Get the maximal number of functions evaluations.
        
        Specified by: getMaxEvaluations in interface ODEIntegrator
        
        Returns:
            maximal number of functions evaluations
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the method.
        
        Specified by: getName in interface ODEIntegrator
        
        Returns:
            name of the method
        
        
        """
        ...
    def getStepEndHandlers(self) -> java.util.List[org.hipparchus.ode.events.ODEStepEndHandler]:
        """
        Get all the handlers for step ends that have been added to the integrator.
        
        Specified by: getStepEndHandlers in interface ODEIntegrator
        
        Returns:
            an unmodifiable list of the added step end handlers
        
        Also see:
            addStepEndHandler,
            clearStepEndHandlers
        
        
        """
        ...
    def getStepHandlers(self) -> java.util.List[org.hipparchus.ode.sampling.ODEStepHandler]:
        """
        Get all the step handlers that have been added to the integrator.
        
        Specified by: getStepHandlers in interface ODEIntegrator
        
        Returns:
            an unmodifiable collection of the added events handlers
        
        Also see:
            addStepHandler, clearStepHandlers
        
        
        """
        ...
    def getStepStart(self) -> 'ODEStateAndDerivative':
        """
        Get the state at step start time t :sub:`i` .
        
        This method can be called during integration (typically by the object implementing the OrdinaryDifferentialEquation problem) if the value of the current step that is attempted is needed.
        
        The result is undefined if the method is called outside of calls to integrate.
        
        Specified by: getStepStart in interface ODEIntegrator
        
        Returns:
            state at step start time t :sub:`i`
        
        
        """
        ...
    def setMaxEvaluations(self, maxEvaluations: int) -> None:
        """
        Set the maximal number of differential equations function evaluations.
        
        The purpose of this method is to avoid infinite loops which can occur for example when stringent error constraints are set or when lots of discrete events are triggered, thus leading to many rejected steps.
        
        Specified by: setMaxEvaluations in interface ODEIntegrator
        
        Parameters:
            maxEvaluations (int): maximal number of function evaluations (negative values are silently converted to maximal integer value, thus
                representing almost unlimited evaluations)
        
        
        """
        ...

class AbstractParameterizable(Parameterizable):
    """
    This abstract class provides boilerplate parameters list.
    """
    def complainIfNotSupported(self, name: str) -> None:
        """
        Check if a parameter is supported and throw an IllegalArgumentException if not.
        
        Parameters:
            name (String): name of the parameter to check
        
        Raises:
            hipparchus: if the parameter is not supported
        
        Also see:
            isSupported
        
        
        """
        ...
    def getParametersNames(self) -> java.util.List[str]:
        """
        Get the names of the supported parameters.
        
        Specified by: getParametersNames in interface Parameterizable
        
        Returns:
            parameters names
        
        Also see:
            isSupported
        
        
        """
        ...
    def isSupported(self, name: str) -> bool:
        """
        Check if a parameter is supported.
        
        Supported parameters are those listed by getParametersNames.
        
        Specified by: isSupported in interface Parameterizable
        
        Parameters:
            name (String): parameter name to check
        
        Returns:
            true if the parameter is supported
        
        Also see:
            getParametersNames
        
        
        """
        ...

class ComplexODEStateAndDerivative(ComplexODEState):
    """
    Container for time, main and secondary state vectors as well as their derivatives.
    
    Also see:
        ComplexOrdinaryDifferentialEquation, ComplexSecondaryODE,
        ODEIntegrator, serialized
    """
    @typing.overload
    def __init__(self, time: float, primaryState: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], primaryDerivative: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray]): ...
    @typing.overload
    def __init__(self, time: float, primaryState: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], primaryDerivative: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], secondaryState: typing.Union[typing.List[typing.MutableSequence[org.hipparchus.complex.Complex]], jpype.JArray], secondaryDerivative: typing.Union[typing.List[typing.MutableSequence[org.hipparchus.complex.Complex]], jpype.JArray]): ...
    def getCompleteDerivative(self) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
        Get complete derivative at time.
        
        Returns:
            complete derivative at time, starting with
            getPrimaryDerivative, followed by all
            getSecondaryDerivative in increasing index order
        
        Also see:
            getPrimaryDerivative,
            getSecondaryDerivative
        
        
        """
        ...
    def getPrimaryDerivative(self) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
        Get derivative of the primary state at time.
        
        Returns:
            derivative of the primary state at time
        
        Also see:
            getSecondaryDerivative,
            getCompleteDerivative
        
        
        """
        ...
    def getSecondaryDerivative(self, index: int) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
        Get derivative of the secondary state at time.
        
        Parameters:
            index (int): index of the secondary set as returned by addSecondaryEquations (beware index
                0 corresponds to primary state, secondary states start at 1)
        
        Returns:
            derivative of the secondary state at time
        
        Also see:
            getPrimaryDerivative,
            getCompleteDerivative
        
        
        """
        ...

_FieldODEStateAndDerivative__T = typing.TypeVar('_FieldODEStateAndDerivative__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEStateAndDerivative(FieldODEState[_FieldODEStateAndDerivative__T], typing.Generic[_FieldODEStateAndDerivative__T]):
    """
    Container for time, main and secondary state vectors as well as their derivatives.
    
    Also see:
        FieldOrdinaryDifferentialEquation, FieldSecondaryODE,
        FieldODEIntegrator
    """
    @typing.overload
    def __init__(self, time: _FieldODEStateAndDerivative__T, primaryState: typing.Union[typing.List[_FieldODEStateAndDerivative__T], jpype.JArray], primaryDerivative: typing.Union[typing.List[_FieldODEStateAndDerivative__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, time: _FieldODEStateAndDerivative__T, primaryState: typing.Union[typing.List[_FieldODEStateAndDerivative__T], jpype.JArray], primaryDerivative: typing.Union[typing.List[_FieldODEStateAndDerivative__T], jpype.JArray], secondaryState: typing.Union[typing.List[typing.MutableSequence[_FieldODEStateAndDerivative__T]], jpype.JArray], secondaryDerivative: typing.Union[typing.List[typing.MutableSequence[_FieldODEStateAndDerivative__T]], jpype.JArray]): ...
    def getCompleteDerivative(self) -> typing.MutableSequence[_FieldODEStateAndDerivative__T]:
        """
        Get complete derivative at time.
        
        Returns:
            complete derivative at time, starting with getPrimaryDerivative,
            followed by all getSecondaryDerivative in increasing index order
        
        Also see:
            getPrimaryDerivative,
            getSecondaryDerivative
        
        
        """
        ...
    def getPrimaryDerivative(self) -> typing.MutableSequence[_FieldODEStateAndDerivative__T]:
        """
        Get derivative of the primary state at time.
        
        Returns:
            derivative of the primary state at time
        
        Also see:
            getSecondaryDerivative,
            getCompleteDerivative
        
        
        """
        ...
    def getSecondaryDerivative(self, index: int) -> typing.MutableSequence[_FieldODEStateAndDerivative__T]:
        """
        Get derivative of the secondary state at time.
        
        Parameters:
            index (int): index of the secondary set as returned by addSecondaryEquations (beware
                index 0 corresponds to primary state, secondary states start at 1)
        
        Returns:
            derivative of the secondary state at time
        
        Also see:
            getPrimaryDerivative,
            getCompleteDerivative
        
        
        """
        ...

class FirstOrderConverter(OrdinaryDifferentialEquation):
    """
    This class converts second order differential equations to first order ones.
    
    This class is a wrapper around a SecondOrderODE which allow to use a ODEIntegrator to integrate it.
    
    The transformation is done by changing the n dimension state vector to a 2n dimension vector, where the first n components are the initial state variables and the n last components are their first time derivative. The first time derivative of this state vector then really contains both the first and second time derivative of the initial state vector, which can be handled by the underlying second order equations set.
    
    One should be aware that the data is duplicated during the transformation process and that for each call to computeDerivatives, this wrapper does copy 4n scalars : 2n before the call to computeSecondDerivatives in order to dispatch the y state vector into z and zDot, and 2n after the call to gather zDot and zDDot into yDot. Since the underlying problem by itself perhaps also needs to copy data and dispatch the arrays into domain objects, this has an impact on both memory and CPU usage. The only way to avoid this duplication is to perform the transformation at the problem level, i.e. to implement the problem as a first order one and then avoid using this class.
    
    Also see:
        ODEIntegrator, OrdinaryDifferentialEquation,
        SecondOrderODE
    """
    def __init__(self, equations: SecondOrderODE):
        """
        Simple constructor. Build a converter around a second order equations set.
        
        Parameters:
            equations (SecondOrderODE): second order equations set to convert
        
        
        """
        ...
    def computeDerivatives(self, t: float, y: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Get the current time derivative of the state vector.
        
        Specified by: computeDerivatives in interface OrdinaryDifferentialEquation
        
        Parameters:
            t (double): current value of the independent time variable
            y (double[]): array containing the current value of the state vector
        
        Returns:
            time derivative of the state vector
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the problem.
        
        The dimension of the first order problem is twice the dimension of the underlying second order problem.
        
        Specified by: getDimension in interface OrdinaryDifferentialEquation
        
        Returns:
            dimension of the problem
        
        
        """
        ...

class NamedParameterJacobianProvider(Parameterizable):
    """
    Interface to compute exactly Jacobian matrix for some parameter when computing VariationalEquation.
    """
    def computeParameterJacobian(self, t: float, y: typing.Union[typing.List[float], jpype.JArray], yDot: typing.Union[typing.List[float], jpype.JArray], paramName: str) -> typing.MutableSequence[float]:
        """
        Compute the Jacobian matrix of ODE with respect to one parameter.
        
        If the parameter does not belong to the collection returned by getParametersNames, the Jacobian will be set to 0, but no errors will be triggered.
        
        Parameters:
            t (double): current value of the independent time variable
            y (double[]): array containing the current value of the main state vector
            yDot (double[]): array containing the current value of the time derivative of the main state vector
            paramName (String): name of the parameter to consider
        
        Returns:
            Jacobian matrix of the ODE with respect to the parameter
        
        Raises:
            hipparchus: if the number of functions evaluations is exceeded
            hipparchus: if arrays dimensions do not match equations settings
            hipparchus: if the parameter is not supported
        
        
        """
        ...

class ODEStateAndDerivative(ODEState):
    """
    Container for time, main and secondary state vectors as well as their derivatives.
    
    Also see:
        OrdinaryDifferentialEquation, SecondaryODE,
        ODEIntegrator, serialized
    """
    @typing.overload
    def __init__(self, time: float, primaryState: typing.Union[typing.List[float], jpype.JArray], primaryDerivative: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, time: float, primaryState: typing.Union[typing.List[float], jpype.JArray], primaryDerivative: typing.Union[typing.List[float], jpype.JArray], secondaryState: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], secondaryDerivative: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    def getCompleteDerivative(self) -> typing.MutableSequence[float]:
        """
        Get complete derivative at time.
        
        Returns:
            complete derivative at time, starting with getPrimaryDerivative,
            followed by all getSecondaryDerivative in increasing index order
        
        Also see:
            getPrimaryDerivative,
            getSecondaryDerivative
        
        
        """
        ...
    def getPrimaryDerivative(self) -> typing.MutableSequence[float]:
        """
        Get derivative of the primary state at time.
        
        Returns:
            derivative of the primary state at time
        
        Also see:
            getSecondaryDerivative,
            getCompleteDerivative
        
        
        """
        ...
    def getSecondaryDerivative(self, index: int) -> typing.MutableSequence[float]:
        """
        Get derivative of the secondary state at time.
        
        Parameters:
            index (int): index of the secondary set as returned by addSecondaryEquations (beware index
                0 corresponds to primary state, secondary states start at 1)
        
        Returns:
            derivative of the secondary state at time
        
        Also see:
            getPrimaryDerivative,
            getCompleteDerivative
        
        
        """
        ...

class ParametersController(Parameterizable):
    """
    Interface to compute by finite difference Jacobian matrix for some parameter when computing VariationalEquation.
    """
    def getParameter(self, name: str) -> float:
        """
        Get parameter value from its name.
        
        Parameters:
            name (String): parameter name
        
        Returns:
            parameter value
        
        Raises:
            hipparchus: if parameter is not supported
        
        
        """
        ...
    def setParameter(self, name: str, value: float) -> None:
        """
        Set the value for a given parameter.
        
        Parameters:
            name (String): parameter name
            value (double): parameter value
        
        Raises:
            hipparchus: if parameter is not supported
        
        
        """
        ...

class ODEJacobiansProvider(OrdinaryDifferentialEquation, NamedParameterJacobianProvider):
    """
    Interface expanding OrdinaryDifferentialEquation in order to compute exactly the Jacobian matrices for VariationalEquation.
    """
    def computeMainStateJacobian(self, t: float, y: typing.Union[typing.List[float], jpype.JArray], yDot: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Compute the Jacobian matrix of ODE with respect to state.
        
        Parameters:
            t (double): current value of the independent time variable
            y (double[]): array containing the current value of the main state vector
            yDot (double[]): array containing the current value of the time derivative of the main state vector
        
        Returns:
            Jacobian matrix of the ODE w.r.t. the main state vector
        
        Raises:
            hipparchus: if the number of functions evaluations is exceeded
            hipparchus: if arrays dimensions do not match equations settings
        
        
        """
        ...
    def computeParameterJacobian(self, t: float, y: typing.Union[typing.List[float], jpype.JArray], yDot: typing.Union[typing.List[float], jpype.JArray], paramName: str) -> typing.MutableSequence[float]:
        """
        Compute the Jacobian matrix of ODE with respect to one parameter.
        
        If the parameter does not belong to the collection returned by getParametersNames, the Jacobian will be set to 0, but no errors will be triggered.
        
        The default implementation supports no parameters at all.
        
        Specified by: computeParameterJacobian in interface NamedParameterJacobianProvider
        
        Parameters:
            t (double): current value of the independent time variable
            y (double[]): array containing the current value of the main state vector
            yDot (double[]): array containing the current value of the time derivative of the main state vector
            paramName (String): name of the parameter to consider
        
        Returns:
            Jacobian matrix of the ODE with respect to the parameter
        
        Raises:
            hipparchus: if arrays dimensions do not match equations settings
        
        
        """
        ...
    def getParametersNames(self) -> java.util.List[str]:
        """
        Get the names of the supported parameters.
        
        The default implementation has no parameters at all.
        
        Specified by: getParametersNames in interface Parameterizable
        
        Returns:
            parameters names
        
        Also see:
            isSupported
        
        
        """
        ...
    def isSupported(self, name: str) -> bool:
        """
        Check if a parameter is supported.
        
        Supported parameters are those listed by getParametersNames.
        
        The default implementation supports no parameters at all.
        
        Specified by: isSupported in interface Parameterizable
        
        Parameters:
            name (String): parameter name to check
        
        Returns:
            true if the parameter is supported
        
        Also see:
            getParametersNames
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.ode")``.

    AbstractFieldIntegrator: typing.Type[AbstractFieldIntegrator]
    AbstractIntegrator: typing.Type[AbstractIntegrator]
    AbstractParameterizable: typing.Type[AbstractParameterizable]
    ComplexODEConverter: typing.Type[ComplexODEConverter]
    ComplexODEState: typing.Type[ComplexODEState]
    ComplexODEStateAndDerivative: typing.Type[ComplexODEStateAndDerivative]
    ComplexOrdinaryDifferentialEquation: typing.Type[ComplexOrdinaryDifferentialEquation]
    ComplexSecondaryODE: typing.Type[ComplexSecondaryODE]
    DenseOutputModel: typing.Type[DenseOutputModel]
    EquationsMapper: typing.Type[EquationsMapper]
    ExpandableODE: typing.Type[ExpandableODE]
    FieldDenseOutputModel: typing.Type[FieldDenseOutputModel]
    FieldEquationsMapper: typing.Type[FieldEquationsMapper]
    FieldExpandableODE: typing.Type[FieldExpandableODE]
    FieldODEIntegrator: typing.Type[FieldODEIntegrator]
    FieldODEState: typing.Type[FieldODEState]
    FieldODEStateAndDerivative: typing.Type[FieldODEStateAndDerivative]
    FieldOrdinaryDifferentialEquation: typing.Type[FieldOrdinaryDifferentialEquation]
    FieldSecondaryODE: typing.Type[FieldSecondaryODE]
    FirstOrderConverter: typing.Type[FirstOrderConverter]
    LocalizedODEFormats: typing.Type[LocalizedODEFormats]
    MultistepFieldIntegrator: typing.Type[MultistepFieldIntegrator]
    MultistepIntegrator: typing.Type[MultistepIntegrator]
    NamedParameterJacobianProvider: typing.Type[NamedParameterJacobianProvider]
    ODEIntegrator: typing.Type[ODEIntegrator]
    ODEJacobiansProvider: typing.Type[ODEJacobiansProvider]
    ODEState: typing.Type[ODEState]
    ODEStateAndDerivative: typing.Type[ODEStateAndDerivative]
    OrdinaryDifferentialEquation: typing.Type[OrdinaryDifferentialEquation]
    ParameterConfiguration: typing.Type[ParameterConfiguration]
    Parameterizable: typing.Type[Parameterizable]
    ParametersController: typing.Type[ParametersController]
    SecondOrderODE: typing.Type[SecondOrderODE]
    SecondaryODE: typing.Type[SecondaryODE]
    VariationalEquation: typing.Type[VariationalEquation]
    events: org.hipparchus.ode.events.__module_protocol__
    nonstiff: org.hipparchus.ode.nonstiff.__module_protocol__
    sampling: org.hipparchus.ode.sampling.__module_protocol__
