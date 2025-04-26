
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
    public classComplexODEConverter extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        This class converts :class:`~org.hipparchus.ode.ComplexOrdinaryDifferentialEquation` into
        :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`.
    
        This class is a wrapper around a :class:`~org.hipparchus.ode.ComplexOrdinaryDifferentialEquation` which allow to use a
        :class:`~org.hipparchus.ode.ODEIntegrator` to integrate it.
    
        The transformation is done by changing the n dimension state vector to a 2n dimension vector, where the even components
        are real parts and odd components are imaginary parts.
    
        One should be aware that the data is duplicated during the transformation process and that for each call to
        :meth:`~org.hipparchus.ode.OrdinaryDifferentialEquation.computeDerivatives`, this wrapper does copy 4n scalars : 2n
        before the call to :meth:`~org.hipparchus.ode.OrdinaryDifferentialEquation.computeDerivatives` in order to dispatch the
        y state vector, and 2n after the call to gather zDot. Since the underlying problem by itself perhaps also needs to copy
        data and dispatch the arrays into domain objects, this has an impact on both memory and CPU usage. The only way to avoid
        this duplication is to perform the transformation at the problem level, i.e. to implement the problem as a first order
        one and then avoid using this class.
    
        The proper way to use the converter is as follows:
    
        .. code-block: java
        
           ODEIntegrator                       integrator       = ...build some integrator...;
           ComplexOrdinaryDifferentialEquation complexEquations = ...set up the complex problem...;
           ComplexODEState                     initialState     = ...set up initial state...;
           ComplexODEConverter                 converter        = new ComplexODEConverter();
           ComplexODEStateAndDerivative        finalstate       =
              converter.convertStateAndDerivative(integrator.integrate(converter.convertEquations(complexEquations),
                                                                       converter.convertState(initialState),
                                                                       t);
         
    
        If there are :class:`~org.hipparchus.ode.ComplexSecondaryODE`, they must be converted too and both the converted primary
        equations and converted secondary equations must be combined together using :class:`~org.hipparchus.ode.ExpandableODE`
        as usual for regular real equations.
    
        Since:
            1.4
    
        Also see:
    
              - :class:`~org.hipparchus.ode.ComplexOrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`
    """
    def __init__(self): ...
    def convertEquations(self, complexOrdinaryDifferentialEquation: 'ComplexOrdinaryDifferentialEquation') -> 'OrdinaryDifferentialEquation':
        """
            Convert an equations set.
        
            Parameters:
                equations (:class:`~org.hipparchus.ode.ComplexOrdinaryDifferentialEquation`): equations to convert
        
            Returns:
                converted equations
        
        
        """
        ...
    def convertSecondaryEquations(self, complexSecondaryODE: 'ComplexSecondaryODE') -> 'SecondaryODE':
        """
            Convert a secondary equations set.
        
            Parameters:
                equations (:class:`~org.hipparchus.ode.ComplexSecondaryODE`): equations to convert
        
            Returns:
                converted equations
        
        
        """
        ...
    @typing.overload
    def convertState(self, oDEStateAndDerivative: 'ODEStateAndDerivative') -> 'ComplexODEStateAndDerivative':
        """
            Convert a complex state (typically the initial state).
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ComplexODEState`): state to convert
        
            Returns:
                converted state
        
            Convert a real state and derivatives (typically the final state or some intermediate state for step handling or event
            handling).
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): state to convert
        
            Returns:
                converted state
        
        
        """
        ...
    @typing.overload
    def convertState(self, complexODEState: 'ComplexODEState') -> 'ODEState': ...

class ComplexODEState(java.io.Serializable):
    """
    public classComplexODEState extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Container for time, main and secondary state vectors.
    
        Since:
            1.4
    
        Also see:
    
              - :class:`~org.hipparchus.ode.ComplexOrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.SecondaryODE`
              - :class:`~org.hipparchus.ode.ODEIntegrator`
              - :class:`~org.hipparchus.ode.ODEStateAndDerivative`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, complexArray: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray]): ...
    @typing.overload
    def __init__(self, double: float, complexArray: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], complexArray2: typing.Union[typing.List[typing.MutableSequence[org.hipparchus.complex.Complex]], jpype.JArray]): ...
    def getCompleteState(self) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
            Get complete state at time.
        
            Returns:
                complete state at time, starting with :meth:`~org.hipparchus.ode.ComplexODEState.getPrimaryState`, followed by all
                :meth:`~org.hipparchus.ode.ComplexODEState.getSecondaryState` in increasing index order
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ComplexODEState.getPrimaryState`
                  - :meth:`~org.hipparchus.ode.ComplexODEState.getSecondaryState`
        
        
        
        """
        ...
    def getCompleteStateDimension(self) -> int:
        """
            Return the dimension of the complete set of equations.
        
            The complete set of equations correspond to the primary set plus all secondary sets.
        
            Returns:
                dimension of the complete set of equations
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ComplexODEState.getPrimaryStateDimension`
                  - :meth:`~org.hipparchus.ode.ComplexODEState.getSecondaryStateDimension`
        
        
        
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
        
                  - :meth:`~org.hipparchus.ode.ComplexODEState.getSecondaryState`
                  - :meth:`~org.hipparchus.ode.ComplexODEState.getCompleteState`
        
        
        
        """
        ...
    def getPrimaryStateDimension(self) -> int:
        """
            Get primary state dimension.
        
            Returns:
                primary state dimension
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ComplexODEState.getSecondaryStateDimension`
                  - :meth:`~org.hipparchus.ode.ComplexODEState.getCompleteStateDimension`
        
        
        
        """
        ...
    def getSecondaryState(self, int: int) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
            Get secondary state at time.
        
            Parameters:
                index (int): index of the secondary set as returned by :meth:`~org.hipparchus.ode.ExpandableODE.addSecondaryEquations` (beware index
                    0 corresponds to primary state, secondary states start at 1)
        
            Returns:
                secondary state at time
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ComplexODEState.getPrimaryState`
                  - :meth:`~org.hipparchus.ode.ComplexODEState.getCompleteState`
        
        
        
        """
        ...
    def getSecondaryStateDimension(self, int: int) -> int:
        """
            Get secondary state dimension.
        
            Parameters:
                index (int): index of the secondary set as returned by :meth:`~org.hipparchus.ode.ExpandableODE.addSecondaryEquations` (beware index
                    0 corresponds to primary state, secondary states start at 1)
        
            Returns:
                secondary state dimension
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ComplexODEState.getPrimaryStateDimension`
                  - :meth:`~org.hipparchus.ode.ComplexODEState.getCompleteStateDimension`
        
        
        
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
    public interfaceComplexOrdinaryDifferentialEquation
    
        This interface represents a first order differential equations set for
        :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`.
    
        Since:
            1.4
    
        Also see:
    
              - :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.ComplexODEConverter`
    """
    def computeDerivatives(self, double: float, complexArray: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray]) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
            Get the current time derivative of the state vector.
        
            Parameters:
                t (double): current value of the independent *time* variable
                y (:class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`[]): array containing the current value of the state vector
        
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
    def init(self, double: float, complexArray: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], double2: float) -> None:
        """
            Initialize equations at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the equations to initialize some internal
            data if needed.
        
            The default implementation does nothing.
        
            Parameters:
                t0 (double): value of the independent *time* variable at integration start
                y0 (:class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`[]): array containing the value of the state vector at integration start
                finalTime (double): target time for the integration
        
        
        """
        ...

class ComplexSecondaryODE:
    """
    public interfaceComplexSecondaryODE
    
        This interface allows users to add secondary differential equations to a primary set of differential equations.
    
        In some cases users may need to integrate some problem-specific equations along with a primary set of differential
        equations. One example is optimal control where adjoined parameters linked to the minimized hamiltonian must be
        integrated.
    
        This interface allows users to add such equations to a primary set of
        :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation` thanks to the
        :meth:`~org.hipparchus.ode.ExpandableODE.addSecondaryEquations` method, after having converted the instance to
        :class:`~org.hipparchus.ode.SecondaryODE`
    
        Since:
            1.4
    
        Also see:
    
              - :class:`~org.hipparchus.ode.ExpandableODE`
              - :class:`~org.hipparchus.ode.ComplexODEConverter`
    """
    def computeDerivatives(self, double: float, complexArray: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], complexArray2: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], complexArray3: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray]) -> typing.MutableSequence[org.hipparchus.complex.Complex]: ...
    def getDimension(self) -> int:
        """
            Get the dimension of the secondary state parameters.
        
            Returns:
                dimension of the secondary state parameters
        
        
        """
        ...
    def init(self, double: float, complexArray: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], complexArray2: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], double2: float) -> None:
        """
            Initialize equations at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the equations to initialize some internal
            data if needed.
        
            The default implementation does nothing.
        
            Parameters:
                t0 (double): value of the independent *time* variable at integration start
                primary0 (:class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`[]): array containing the value of the primary state vector at integration start
                secondary0 (:class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`[]): array containing the value of the secondary state vector at integration start
                finalTime (double): target time for the integration
        
        
        """
        ...

class DenseOutputModel(org.hipparchus.ode.sampling.ODEStepHandler, java.io.Serializable):
    """
    public classDenseOutputModel extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.sampling.ODEStepHandler`, :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        This class stores all information provided by an ODE integrator during the integration process and build a continuous
        model of the solution from this.
    
        This class act as a step handler from the integrator point of view. It is called iteratively during the integration
        process and stores a copy of all steps information in a sorted collection for later use. Once the integration process is
        over, the user can use the :meth:`~org.hipparchus.ode.DenseOutputModel.getInterpolatedState` method to retrieve this
        information at any time. It is important to wait for the integration to be over before attempting to call
        :meth:`~org.hipparchus.ode.DenseOutputModel.getInterpolatedState` because some internal variables are set only once the
        last step has been handled.
    
        This is useful for example if the main loop of the user application should remain independent from the integration
        process or if one needs to mimic the behaviour of an analytical model despite a numerical model is used (i.e. one needs
        the ability to get the model value at any time or to navigate through the data).
    
        If problem modeling is done with several separate integration phases for contiguous intervals, the same DenseOutputModel
        can be used as step handler for all integration phases as long as they are performed in order and in the same direction.
        As an example, one can extrapolate the trajectory of a satellite with one model (i.e. one set of differential equations)
        up to the beginning of a maneuver, use another more complex model including thrusters modeling and accurate attitude
        control during the maneuver, and revert to the first model after the end of the maneuver. If the same continuous output
        model handles the steps of all integration phases, the user do not need to bother when the maneuver begins or ends, he
        has all the data available in a transparent manner.
    
        An important feature of this class is that it implements the :code:`Serializable` interface. This means that the result
        of an integration can be serialized and reused later (if stored into a persistent medium like a filesystem or a
        database) or elsewhere (if sent to another application). Only the result of the integration is stored, there is no
        reference to the integrated problem by itself.
    
        One should be aware that the amount of data stored in a DenseOutputModel instance can be important if the state vector
        is large, if the integration interval is long or if the steps are small (which can result from small tolerance settings
        in :class:`~org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator`).
    
        Also see:
    
              - :class:`~org.hipparchus.ode.sampling.ODEStepHandler`
              - :class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`
              - :meth:`~serialized`
    """
    def __init__(self): ...
    def append(self, denseOutputModel: 'DenseOutputModel') -> None: ...
    def finish(self, oDEStateAndDerivative: 'ODEStateAndDerivative') -> None:
        """
            Finalize integration.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.ODEStepHandler.finish` in
                interface :class:`~org.hipparchus.ode.sampling.ODEStepHandler`
        
            Parameters:
                finalState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): state at integration end
        
        
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
    def getInterpolatedState(self, double: float) -> 'ODEStateAndDerivative':
        """
            Get the state at interpolated time.
        
            Parameters:
                time (double): time of the interpolated point
        
            Returns:
                state at interpolated time
        
        
        """
        ...
    def handleStep(self, oDEStateInterpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> None:
        """
            Handle the last accepted step.
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.ODEStepHandler.handleStep` in
                interface :class:`~org.hipparchus.ode.sampling.ODEStepHandler`
        
            Parameters:
                interpolator (:class:`~org.hipparchus.ode.sampling.ODEStateInterpolator`): interpolator for the last accepted step
        
        
        """
        ...
    def init(self, oDEStateAndDerivative: 'ODEStateAndDerivative', double: float) -> None:
        """
            Initialize step handler at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the step handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.hipparchus.ode.sampling.ODEStepHandler.init` in
                interface :class:`~org.hipparchus.ode.sampling.ODEStepHandler`
        
            Parameters:
                initialState (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): initial time, state vector and derivative
                targetTime (double): target time for the integration
        
        
        """
        ...

class EquationsMapper(java.io.Serializable):
    """
    public classEquationsMapper extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Class mapping the part of a complete state or derivative that pertains to a specific differential equation.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.SecondaryODE`
              - :meth:`~serialized`
    """
    def extractEquationData(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
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
    def insertEquationData(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    def mapStateAndDerivative(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> 'ODEStateAndDerivative': ...

class ExpandableODE:
    """
    public classExpandableODE extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        This class represents a combined set of first order differential equations, with at least a primary set of equations
        expandable by some sets of secondary equations.
    
        One typical use case is the computation of the Jacobian matrix for some ODE. In this case, the primary set of equations
        corresponds to the raw ODE, and we add to this set another bunch of secondary equations which represent the Jacobian
        matrix of the primary set.
    
        We want the integrator to use *only* the primary set to estimate the errors and hence the step sizes. It should *not*
        use the secondary equations in this computation. The :class:`~org.hipparchus.ode.AbstractIntegrator` will be able to
        know where the primary set ends and so where the secondary sets begin.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.VariationalEquation`
    """
    def __init__(self, ordinaryDifferentialEquation: 'OrdinaryDifferentialEquation'): ...
    def addSecondaryEquations(self, secondaryODE: 'SecondaryODE') -> int:
        """
            Add a set of secondary equations to be integrated along with the primary set.
        
            Parameters:
                secondary (:class:`~org.hipparchus.ode.SecondaryODE`): secondary equations set
        
            Returns:
                index of the secondary equation in the expanded state, to be used as the parameter to
                :meth:`~org.hipparchus.ode.FieldODEState.getSecondaryState` and
                :meth:`~org.hipparchus.ode.FieldODEStateAndDerivative.getSecondaryDerivative` (beware index 0 corresponds to primary
                state, secondary states start at 1)
        
        
        """
        ...
    def computeDerivatives(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
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
    def init(self, oDEState: 'ODEState', double: float) -> None:
        """
            Initialize equations at the start of an ODE integration.
        
            Parameters:
                s0 (:class:`~org.hipparchus.ode.ODEState`): state at integration start
                finalTime (double): target time for the integration
        
            Raises:
                :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`: if the number of functions evaluations is exceeded
                :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`: if arrays dimensions do not match equations settings
        
        
        """
        ...

_FieldDenseOutputModel__T = typing.TypeVar('_FieldDenseOutputModel__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDenseOutputModel(org.hipparchus.ode.sampling.FieldODEStepHandler[_FieldDenseOutputModel__T], typing.Generic[_FieldDenseOutputModel__T]):
    """
    public classFieldDenseOutputModel<T extends :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.sampling.FieldODEStepHandler`<T>
    
        This class stores all information provided by an ODE integrator during the integration process and build a continuous
        model of the solution from this.
    
        This class act as a step handler from the integrator point of view. It is called iteratively during the integration
        process and stores a copy of all steps information in a sorted collection for later use. Once the integration process is
        over, the user can use the :meth:`~org.hipparchus.ode.FieldDenseOutputModel.getInterpolatedState` method to retrieve
        this information at any time. It is important to wait for the integration to be over before attempting to call
        :meth:`~org.hipparchus.ode.FieldDenseOutputModel.getInterpolatedState` because some internal variables are set only once
        the last step has been handled.
    
        This is useful for example if the main loop of the user application should remain independent from the integration
        process or if one needs to mimic the behaviour of an analytical model despite a numerical model is used (i.e. one needs
        the ability to get the model value at any time or to navigate through the data).
    
        If problem modeling is done with several separate integration phases for contiguous intervals, the same
        FieldDenseOutputModel can be used as step handler for all integration phases as long as they are performed in order and
        in the same direction. As an example, one can extrapolate the trajectory of a satellite with one model (i.e. one set of
        differential equations) up to the beginning of a maneuver, use another more complex model including thrusters modeling
        and accurate attitude control during the maneuver, and revert to the first model after the end of the maneuver. If the
        same continuous output model handles the steps of all integration phases, the user do not need to bother when the
        maneuver begins or ends, he has all the data available in a transparent manner.
    
        One should be aware that the amount of data stored in a FieldDenseOutputModel instance can be important if the state
        vector is large, if the integration interval is long or if the steps are small (which can result from small tolerance
        settings in :class:`~org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator`).
    
        Also see:
    
              - :class:`~org.hipparchus.ode.sampling.FieldODEStepHandler`
              - :class:`~org.hipparchus.ode.sampling.FieldODEStateInterpolator`
    """
    def __init__(self): ...
    def append(self, fieldDenseOutputModel: 'FieldDenseOutputModel'[_FieldDenseOutputModel__T]) -> None: ...
    def finish(self, fieldODEStateAndDerivative: 'FieldODEStateAndDerivative'[_FieldDenseOutputModel__T]) -> None: ...
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
    def getInterpolatedState(self, t: _FieldDenseOutputModel__T) -> 'FieldODEStateAndDerivative'[_FieldDenseOutputModel__T]: ...
    def handleStep(self, fieldODEStateInterpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldDenseOutputModel__T]) -> None: ...
    def init(self, fieldODEStateAndDerivative: 'FieldODEStateAndDerivative'[_FieldDenseOutputModel__T], t: _FieldDenseOutputModel__T) -> None: ...

_FieldEquationsMapper__T = typing.TypeVar('_FieldEquationsMapper__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEquationsMapper(java.io.Serializable, typing.Generic[_FieldEquationsMapper__T]):
    """
    public classFieldEquationsMapper<T extends :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Class mapping the part of a complete state or derivative that pertains to a set of differential equations.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.FieldExpandableODE`
              - :meth:`~serialized`
    """
    def extractEquationData(self, int: int, tArray: typing.Union[typing.List[_FieldEquationsMapper__T], jpype.JArray]) -> typing.MutableSequence[_FieldEquationsMapper__T]: ...
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
    def insertEquationData(self, int: int, tArray: typing.Union[typing.List[_FieldEquationsMapper__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldEquationsMapper__T], jpype.JArray]) -> None: ...
    def mapStateAndDerivative(self, t: _FieldEquationsMapper__T, tArray: typing.Union[typing.List[_FieldEquationsMapper__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldEquationsMapper__T], jpype.JArray]) -> 'FieldODEStateAndDerivative'[_FieldEquationsMapper__T]: ...

_FieldExpandableODE__T = typing.TypeVar('_FieldExpandableODE__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldExpandableODE(typing.Generic[_FieldExpandableODE__T]):
    """
    public classFieldExpandableODE<T extends :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        This class represents a combined set of first order differential equations, with at least a primary set of equations
        expandable by some sets of secondary equations.
    
        One typical use case is the computation of the Jacobian matrix for some ODE. In this case, the primary set of equations
        corresponds to the raw ODE, and we add to this set another bunch of secondary equations which represent the Jacobian
        matrix of the primary set.
    
        We want the integrator to use *only* the primary set to estimate the errors and hence the step sizes. It should *not*
        use the secondary equations in this computation. The :class:`~org.hipparchus.ode.FieldODEIntegrator` will be able to
        know where the primary set ends and so where the secondary sets begin.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.FieldSecondaryODE`
    """
    def __init__(self, fieldOrdinaryDifferentialEquation: 'FieldOrdinaryDifferentialEquation'[_FieldExpandableODE__T]): ...
    def addSecondaryEquations(self, fieldSecondaryODE: 'FieldSecondaryODE'[_FieldExpandableODE__T]) -> int: ...
    def computeDerivatives(self, t: _FieldExpandableODE__T, tArray: typing.Union[typing.List[_FieldExpandableODE__T], jpype.JArray]) -> typing.MutableSequence[_FieldExpandableODE__T]: ...
    def getMapper(self) -> FieldEquationsMapper[_FieldExpandableODE__T]: ...
    def getPrimary(self) -> 'FieldOrdinaryDifferentialEquation'[_FieldExpandableODE__T]: ...
    def init(self, fieldODEState: 'FieldODEState'[_FieldExpandableODE__T], t: _FieldExpandableODE__T) -> None: ...

_FieldODEIntegrator__T = typing.TypeVar('_FieldODEIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEIntegrator(typing.Generic[_FieldODEIntegrator__T]):
    """
    public interfaceFieldODEIntegrator<T extends :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`<T>>
    
        This interface represents a first order integrator for differential equations.
    
        The classes which are devoted to solve first order differential equations should implement this interface. The problems
        which can be handled should implement the :class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation` interface.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation`
    """
    def addEventDetector(self, fieldODEEventDetector: org.hipparchus.ode.events.FieldODEEventDetector[_FieldODEIntegrator__T]) -> None: ...
    def addStepEndHandler(self, fieldODEStepEndHandler: typing.Union[org.hipparchus.ode.events.FieldODEStepEndHandler[_FieldODEIntegrator__T], typing.Callable[['FieldODEStateAndDerivative'[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]]) -> None: ...
    def addStepHandler(self, fieldODEStepHandler: typing.Union[org.hipparchus.ode.sampling.FieldODEStepHandler[_FieldODEIntegrator__T], typing.Callable[[org.hipparchus.ode.sampling.FieldODEStateInterpolator[org.hipparchus.CalculusFieldElement]], None]]) -> None: ...
    def clearEventDetectors(self) -> None:
        """
            Remove all the event handlers that have been added to the integrator.
        
            Since:
                3.0
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.FieldODEIntegrator.addEventDetector`
                  - :meth:`~org.hipparchus.ode.FieldODEIntegrator.getEventDetectors`
        
        
        
        """
        ...
    def clearStepEndHandlers(self) -> None:
        """
            Remove all the handlers for step ends that have been added to the integrator.
        
            Since:
                3.0
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.FieldODEIntegrator.addStepEndHandler`
                  - :meth:`~org.hipparchus.ode.FieldODEIntegrator.getStepEndHandlers`
        
        
        
        """
        ...
    def clearStepHandlers(self) -> None:
        """
            Remove all the step handlers that have been added to the integrator.
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.FieldODEIntegrator.addStepHandler`
                  - :meth:`~org.hipparchus.ode.FieldODEIntegrator.getStepHandlers`
        
        
        
        """
        ...
    def getCurrentSignedStepsize(self) -> _FieldODEIntegrator__T:
        """
            Get the current signed value of the integration stepsize.
        
            This method can be called during integration (typically by the object implementing the
            :class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation` problem) if the signed value of the current stepsize that
            is tried is needed.
        
            The result is undefined if the method is called outside of calls to :code:`integrate`.
        
            Returns:
                current signed value of the stepsize
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
            Get the number of evaluations of the differential equations function.
        
            The number of evaluations corresponds to the last call to the :code:`integrate` method. It is 0 if the method has not
            been called yet.
        
            Returns:
                number of evaluations of the differential equations function
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.List[org.hipparchus.ode.events.FieldODEEventDetector[_FieldODEIntegrator__T]]: ...
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
    def getStepEndHandlers(self) -> java.util.List[org.hipparchus.ode.events.FieldODEStepEndHandler[_FieldODEIntegrator__T]]: ...
    def getStepHandlers(self) -> java.util.List[org.hipparchus.ode.sampling.FieldODEStepHandler[_FieldODEIntegrator__T]]: ...
    def getStepStart(self) -> 'FieldODEStateAndDerivative'[_FieldODEIntegrator__T]: ...
    def integrate(self, fieldExpandableODE: FieldExpandableODE[_FieldODEIntegrator__T], fieldODEState: 'FieldODEState'[_FieldODEIntegrator__T], t: _FieldODEIntegrator__T) -> 'FieldODEStateAndDerivative'[_FieldODEIntegrator__T]: ...
    def setMaxEvaluations(self, int: int) -> None:
        """
            Set the maximal number of differential equations function evaluations.
        
            The purpose of this method is to avoid infinite loops which can occur for example when stringent error constraints are
            set or when lots of discrete events are triggered, thus leading to many rejected steps.
        
            Parameters:
                maxEvaluations (int): maximal number of function evaluations (negative values are silently converted to maximal integer value, thus
                    representing almost unlimited evaluations)
        
        
        """
        ...

_FieldODEState__T = typing.TypeVar('_FieldODEState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEState(typing.Generic[_FieldODEState__T]):
    """
    public classFieldODEState<T extends :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Container for time, main and secondary state vectors.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.FieldSecondaryODE`
              - :class:`~org.hipparchus.ode.FieldODEIntegrator`
              - :class:`~org.hipparchus.ode.FieldODEStateAndDerivative`
    """
    @typing.overload
    def __init__(self, t: _FieldODEState__T, tArray: typing.Union[typing.List[_FieldODEState__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, t: _FieldODEState__T, tArray: typing.Union[typing.List[_FieldODEState__T], jpype.JArray], tArray2: typing.Union[typing.List[typing.MutableSequence[_FieldODEState__T]], jpype.JArray]): ...
    def getCompleteState(self) -> typing.MutableSequence[_FieldODEState__T]:
        """
            Get complete state at time.
        
            Returns:
                complete state at time, starting with :meth:`~org.hipparchus.ode.FieldODEState.getPrimaryState`, followed by all
                :meth:`~org.hipparchus.ode.FieldODEState.getSecondaryState` in increasing index order
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.FieldODEState.getPrimaryState`
                  - :meth:`~org.hipparchus.ode.FieldODEState.getSecondaryState`
        
        
        
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
        
                  - :meth:`~org.hipparchus.ode.FieldODEState.getSecondaryState`
                  - :meth:`~org.hipparchus.ode.FieldODEState.getCompleteState`
        
        
        
        """
        ...
    def getPrimaryStateDimension(self) -> int:
        """
            Get primary state dimension.
        
            Returns:
                primary state dimension
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.FieldODEState.getSecondaryStateDimension`
                  - :meth:`~org.hipparchus.ode.FieldODEState.getCompleteStateDimension`
        
        
        
        """
        ...
    def getSecondaryState(self, int: int) -> typing.MutableSequence[_FieldODEState__T]:
        """
            Get secondary state at time.
        
            Parameters:
                index (int): index of the secondary set as returned by :meth:`~org.hipparchus.ode.FieldExpandableODE.addSecondaryEquations` (beware
                    index 0 corresponds to primary state, secondary states start at 1)
        
            Returns:
                secondary state at time
        
        
        """
        ...
    def getSecondaryStateDimension(self, int: int) -> int:
        """
            Get secondary state dimension.
        
            Parameters:
                index (int): index of the secondary set as returned by :meth:`~org.hipparchus.ode.FieldExpandableODE.addSecondaryEquations` (beware
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
    public interfaceFieldOrdinaryDifferentialEquation<T extends :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`<T>>
    
        This interface represents a first order differential equations set.
    
        This interface should be implemented by all real first order differential equation problems before they can be handled
        by the integrators :meth:`~org.hipparchus.ode.FieldODEIntegrator.integrate` method.
    
        A first order differential equations problem, as seen by an integrator is the time derivative :code:`dY/dt` of a state
        vector :code:`Y`, both being one dimensional arrays. From the integrator point of view, this derivative depends only on
        the current time :code:`t` and on the state vector :code:`Y`.
    
        For real problems, the derivative depends also on parameters that do not belong to the state vector (dynamical model
        constants for example). These constants are completely outside of the scope of this interface, the classes that
        implement it are allowed to handle them as they want.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.FieldODEIntegrator`
    """
    def computeDerivatives(self, t: _FieldOrdinaryDifferentialEquation__T, tArray: typing.Union[typing.List[_FieldOrdinaryDifferentialEquation__T], jpype.JArray]) -> typing.MutableSequence[_FieldOrdinaryDifferentialEquation__T]:
        """
            Get the current time derivative of the state vector.
        
            Parameters:
                t (:class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation`): current value of the independent *time* variable
                y (:class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation`[]): array containing the current value of the state vector
        
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
    def init(self, t: _FieldOrdinaryDifferentialEquation__T, tArray: typing.Union[typing.List[_FieldOrdinaryDifferentialEquation__T], jpype.JArray], t3: _FieldOrdinaryDifferentialEquation__T) -> None:
        """
            Initialize equations at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the equations to initialize some internal
            data if needed.
        
            The default implementation does nothing.
        
            Parameters:
                t0 (:class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation`): value of the independent *time* variable at integration start
                y0 (:class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation`[]): array containing the value of the state vector at integration start
                finalTime (:class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation`): target time for the integration
        
        
        """
        ...

_FieldSecondaryODE__T = typing.TypeVar('_FieldSecondaryODE__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldSecondaryODE(typing.Generic[_FieldSecondaryODE__T]):
    """
    public interfaceFieldSecondaryODE<T extends :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`<T>>
    
        This interface allows users to add secondary differential equations to a primary set of differential equations.
    
        In some cases users may need to integrate some problem-specific equations along with a primary set of differential
        equations. One example is optimal control where adjoined parameters linked to the minimized Hamiltonian must be
        integrated.
    
        This interface allows users to add such equations to a primary set of
        :class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation` thanks to the
        :meth:`~org.hipparchus.ode.FieldExpandableODE.addSecondaryEquations` method.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.FieldExpandableODE`
    """
    def computeDerivatives(self, t: _FieldSecondaryODE__T, tArray: typing.Union[typing.List[_FieldSecondaryODE__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldSecondaryODE__T], jpype.JArray], tArray3: typing.Union[typing.List[_FieldSecondaryODE__T], jpype.JArray]) -> typing.MutableSequence[_FieldSecondaryODE__T]: ...
    def getDimension(self) -> int:
        """
            Get the dimension of the secondary state parameters.
        
            Returns:
                dimension of the secondary state parameters
        
        
        """
        ...
    def init(self, t: _FieldSecondaryODE__T, tArray: typing.Union[typing.List[_FieldSecondaryODE__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldSecondaryODE__T], jpype.JArray], t4: _FieldSecondaryODE__T) -> None:
        """
            Initialize equations at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the equations to initialize some internal
            data if needed.
        
            The default implementation does nothing.
        
            Parameters:
                t0 (:class:`~org.hipparchus.ode.FieldSecondaryODE`): value of the independent *time* variable at integration start
                primary0 (:class:`~org.hipparchus.ode.FieldSecondaryODE`[]): array containing the value of the primary state vector at integration start
                secondary0 (:class:`~org.hipparchus.ode.FieldSecondaryODE`[]): array containing the value of the secondary state vector at integration start
                finalTime (:class:`~org.hipparchus.ode.FieldSecondaryODE`): target time for the integration
        
        
        """
        ...

class LocalizedODEFormats(java.lang.Enum['LocalizedODEFormats'], org.hipparchus.exception.Localizable):
    """
    public enumLocalizedODEFormats extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum`<:class:`~org.hipparchus.ode.LocalizedODEFormats`>
    implements :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`
    
        Enumeration for localized messages formats used in exceptions messages.
    
        The constants in this enumeration represent the available formats as localized strings. These formats are intended to be
        localized using simple properties files, using the constant name as the key and the property value as the message
        format. The source English format is provided in the constants themselves to serve both as a reminder for developers to
        understand the parameters needed by each format, as a basis for translators to create localized properties files, and as
        a default format if some translation is missing.
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
        
            Specified by:
                :meth:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
        
            Specified by:
                :meth:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LocalizedODEFormats':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['LocalizedODEFormats']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared.
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_MultistepFieldIntegrator__T = typing.TypeVar('_MultistepFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class MultistepFieldIntegrator(org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator[_MultistepFieldIntegrator__T], typing.Generic[_MultistepFieldIntegrator__T]):
    """
    public abstract classMultistepFieldIntegrator<T extends :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator`<T>
    
        This class is the base class for multistep integrators for Ordinary Differential Equations.
    
        We define scaled derivatives s :sub:`i` (n) at step n as: \[ \left\{\begin{align} s_1(n) &= h y'_n \text{ for first
        derivative}\\ s_2(n) &= \frac{h^2}{2} y_n'' \text{ for second derivative}\\ s_3(n) &= \frac{h^3}{6} y_n''' \text{ for
        third derivative}\\ &\cdots\\ s_k(n) &= \frac{h^k}{k!} y_n^{(k)} \text{ for } k^\mathrm{th} \text{ derivative}
        \end{align}\right. \]
    
        Rather than storing several previous steps separately, this implementation uses the Nordsieck vector with higher degrees
        scaled derivatives all taken at the same step (y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined
        as: \[ r_n = [ s_2(n), s_3(n) \ldots s_k(n) ]^T \] (we omit the k index in the notation for clarity)
    
        Multistep integrators with Nordsieck representation are highly sensitive to large step changes because when the step is
        multiplied by factor a, the k :sup:`th` component of the Nordsieck vector is multiplied by a :sup:`k` and the last
        components are the least accurate ones. The default max growth factor is therefore set to a quite low value: 2
        :sup:`1/order` .
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.AdamsBashforthFieldIntegrator`
              - :class:`~org.hipparchus.ode.nonstiff.AdamsMoultonFieldIntegrator`
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
    def getStarterIntegrator(self) -> FieldODEIntegrator[_MultistepFieldIntegrator__T]: ...
    def setMaxGrowth(self, double: float) -> None:
        """
            Set the maximal growth factor for stepsize control.
        
            Parameters:
                maxGrowth (double): maximal growth factor
        
        
        """
        ...
    def setMinReduction(self, double: float) -> None:
        """
            Set the minimal reduction factor for stepsize control.
        
            Parameters:
                minReduction (double): minimal reduction factor
        
        
        """
        ...
    def setSafety(self, double: float) -> None:
        """
            Set the safety factor for stepsize control.
        
            Parameters:
                safety (double): safety factor
        
        
        """
        ...
    def setStarterIntegrator(self, fieldODEIntegrator: FieldODEIntegrator[_MultistepFieldIntegrator__T]) -> None: ...

class MultistepIntegrator(org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator):
    """
    public abstract classMultistepIntegrator extends :class:`~org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator`
    
        This class is the base class for multistep integrators for Ordinary Differential Equations.
    
        We define scaled derivatives s :sub:`i` (n) at step n as: \[ \left\{\begin{align} s_1(n) &= h y'_n \text{ for first
        derivative}\\ s_2(n) &= \frac{h^2}{2} y_n'' \text{ for second derivative}\\ s_3(n) &= \frac{h^3}{6} y_n''' \text{ for
        third derivative}\\ &\cdots\\ s_k(n) &= \frac{h^k}{k!} y_n^{(k)} \text{ for } k^\mathrm{th} \text{ derivative}
        \end{align}\right. \]
    
        Rather than storing several previous steps separately, this implementation uses the Nordsieck vector with higher degrees
        scaled derivatives all taken at the same step (y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined
        as: \[ r_n = [ s_2(n), s_3(n) \ldots s_k(n) ]^T \] (we omit the k index in the notation for clarity)
    
        Multistep integrators with Nordsieck representation are highly sensitive to large step changes because when the step is
        multiplied by factor a, the k :sup:`th` component of the Nordsieck vector is multiplied by a :sup:`k` and the last
        components are the least accurate ones. The default max growth factor is therefore set to a quite low value: 2
        :sup:`1/order` .
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.AdamsBashforthIntegrator`
              - :class:`~org.hipparchus.ode.nonstiff.AdamsMoultonIntegrator`
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
    def setMaxGrowth(self, double: float) -> None:
        """
            Set the maximal growth factor for stepsize control.
        
            Parameters:
                maxGrowth (double): maximal growth factor
        
        
        """
        ...
    def setMinReduction(self, double: float) -> None:
        """
            Set the minimal reduction factor for stepsize control.
        
            Parameters:
                minReduction (double): minimal reduction factor
        
        
        """
        ...
    def setSafety(self, double: float) -> None:
        """
            Set the safety factor for stepsize control.
        
            Parameters:
                safety (double): safety factor
        
        
        """
        ...
    def setStarterIntegrator(self, oDEIntegrator: 'ODEIntegrator') -> None:
        """
            Set the starter integrator.
        
            The various step and event handlers for this starter integrator will be managed automatically by the multi-step
            integrator. Any user configuration for these elements will be cleared before use.
        
            Parameters:
                starterIntegrator (:class:`~org.hipparchus.ode.ODEIntegrator`): starter integrator
        
        
        """
        ...

class ODEIntegrator:
    """
    public interfaceODEIntegrator
    
        This interface represents a first order integrator for differential equations.
    
        The classes which are devoted to solve first order differential equations should implement this interface. The problems
        which can be handled should implement the :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation` interface.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.sampling.ODEStepHandler`
              - :class:`~org.hipparchus.ode.events.ODEEventHandler`
    """
    def addEventDetector(self, oDEEventDetector: org.hipparchus.ode.events.ODEEventDetector) -> None:
        """
            Add an event detector to the integrator.
        
            Parameters:
                detector (:class:`~org.hipparchus.ode.events.ODEEventDetector`): event detector
        
            Since:
                3.0
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.getEventDetectors`
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.clearEventDetectors`
        
        
        
        """
        ...
    def addStepEndHandler(self, oDEStepEndHandler: typing.Union[org.hipparchus.ode.events.ODEStepEndHandler, typing.Callable]) -> None:
        """
            Add a handler for step ends to the integrator.
        
            The :meth:`~org.hipparchus.ode.events.ODEStepEndHandler.stepEndOccurred` method of the :code:`handler` will be called at
            each step end.
        
            Parameters:
                handler (:class:`~org.hipparchus.ode.events.ODEStepEndHandler`): handler for step ends
        
            Since:
                3.0
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.getStepEndHandlers`
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.clearStepEndHandlers`
        
        
        
        """
        ...
    def addStepHandler(self, oDEStepHandler: typing.Union[org.hipparchus.ode.sampling.ODEStepHandler, typing.Callable]) -> None:
        """
            Add a step handler to this integrator.
        
            The handler will be called by the integrator for each accepted step.
        
            Parameters:
                handler (:class:`~org.hipparchus.ode.sampling.ODEStepHandler`): handler for the accepted steps
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.getStepHandlers`
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.clearStepHandlers`
        
        
        
        """
        ...
    def clearEventDetectors(self) -> None:
        """
            Remove all the event handlers that have been added to the integrator.
        
            Since:
                3.0
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.addEventDetector`
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.getEventDetectors`
        
        
        
        """
        ...
    def clearStepEndHandlers(self) -> None:
        """
            Remove all the handlers for step ends that have been added to the integrator.
        
            Since:
                3.0
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.addStepEndHandler`
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.getStepEndHandlers`
        
        
        
        """
        ...
    def clearStepHandlers(self) -> None:
        """
            Remove all the step handlers that have been added to the integrator.
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.addStepHandler`
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.getStepHandlers`
        
        
        
        """
        ...
    def getCurrentSignedStepsize(self) -> float:
        """
            Get the current signed value of the integration stepsize.
        
            This method can be called during integration (typically by the object implementing the
            :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation` problem) if the signed value of the current stepsize that is
            tried is needed.
        
            The result is undefined if the method is called outside of calls to :code:`integrate`.
        
            Returns:
                current signed value of the stepsize
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
            Get the number of evaluations of the differential equations function.
        
            The number of evaluations corresponds to the last call to the :code:`integrate` method. It is 0 if the method has not
            been called yet.
        
            Returns:
                number of evaluations of the differential equations function
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.List[org.hipparchus.ode.events.ODEEventDetector]: ...
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
    def getStepEndHandlers(self) -> java.util.List[org.hipparchus.ode.events.ODEStepEndHandler]: ...
    def getStepHandlers(self) -> java.util.List[org.hipparchus.ode.sampling.ODEStepHandler]: ...
    def getStepStart(self) -> 'ODEStateAndDerivative':
        """
            Get the state at step start time t :sub:`i` .
        
            This method can be called during integration (typically by the object implementing the
            :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation` problem) if the value of the current step that is attempted is
            needed.
        
            The result is undefined if the method is called outside of calls to :code:`integrate`.
        
            Returns:
                state at step start time t :sub:`i`
        
        
        """
        ...
    @typing.overload
    def integrate(self, expandableODE: ExpandableODE, oDEState: 'ODEState', double: float) -> 'ODEStateAndDerivative': ...
    @typing.overload
    def integrate(self, ordinaryDifferentialEquation: 'OrdinaryDifferentialEquation', oDEState: 'ODEState', double: float) -> 'ODEStateAndDerivative': ...
    def setMaxEvaluations(self, int: int) -> None:
        """
            Set the maximal number of differential equations function evaluations.
        
            The purpose of this method is to avoid infinite loops which can occur for example when stringent error constraints are
            set or when lots of discrete events are triggered, thus leading to many rejected steps.
        
            Parameters:
                maxEvaluations (int): maximal number of function evaluations (negative values are silently converted to maximal integer value, thus
                    representing almost unlimited evaluations)
        
        
        """
        ...

class ODEState(java.io.Serializable):
    """
    public classODEState extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Container for time, main and secondary state vectors.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.SecondaryODE`
              - :class:`~org.hipparchus.ode.ODEIntegrator`
              - :class:`~org.hipparchus.ode.ODEStateAndDerivative`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    def getCompleteState(self) -> typing.MutableSequence[float]:
        """
            Get complete state at time.
        
            Returns:
                complete state at time, starting with :meth:`~org.hipparchus.ode.ODEState.getPrimaryState`, followed by all
                :meth:`~org.hipparchus.ode.ODEState.getSecondaryState` in increasing index order
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEState.getPrimaryState`
                  - :meth:`~org.hipparchus.ode.ODEState.getSecondaryState`
        
        
        
        """
        ...
    def getCompleteStateDimension(self) -> int:
        """
            Return the dimension of the complete set of equations.
        
            The complete set of equations correspond to the primary set plus all secondary sets.
        
            Returns:
                dimension of the complete set of equations
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEState.getPrimaryStateDimension`
                  - :meth:`~org.hipparchus.ode.ODEState.getSecondaryStateDimension`
        
        
        
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
        
                  - :meth:`~org.hipparchus.ode.ODEState.getSecondaryState`
                  - :meth:`~org.hipparchus.ode.ODEState.getCompleteState`
        
        
        
        """
        ...
    def getPrimaryStateDimension(self) -> int:
        """
            Get primary state dimension.
        
            Returns:
                primary state dimension
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEState.getSecondaryStateDimension`
                  - :meth:`~org.hipparchus.ode.ODEState.getCompleteStateDimension`
        
        
        
        """
        ...
    def getSecondaryState(self, int: int) -> typing.MutableSequence[float]:
        """
            Get secondary state at time.
        
            Parameters:
                index (int): index of the secondary set as returned by :meth:`~org.hipparchus.ode.ExpandableODE.addSecondaryEquations` (beware index
                    0 corresponds to primary state, secondary states start at 1)
        
            Returns:
                secondary state at time
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEState.getPrimaryState`
                  - :meth:`~org.hipparchus.ode.ODEState.getCompleteState`
        
        
        
        """
        ...
    def getSecondaryStateDimension(self, int: int) -> int:
        """
            Get secondary state dimension.
        
            Parameters:
                index (int): index of the secondary set as returned by :meth:`~org.hipparchus.ode.ExpandableODE.addSecondaryEquations` (beware index
                    0 corresponds to primary state, secondary states start at 1)
        
            Returns:
                secondary state dimension
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEState.getPrimaryStateDimension`
                  - :meth:`~org.hipparchus.ode.ODEState.getCompleteStateDimension`
        
        
        
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
    public interfaceOrdinaryDifferentialEquation
    
        This interface represents a first order differential equations set.
    
        This interface should be implemented by all real first order differential equation problems before they can be handled
        by the integrators :meth:`~org.hipparchus.ode.ODEIntegrator.integrate` method.
    
        A first order differential equations problem, as seen by an integrator is the time derivative :code:`dY/dt` of a state
        vector :code:`Y`, both being one dimensional arrays. From the integrator point of view, this derivative depends only on
        the current time :code:`t` and on the state vector :code:`Y`.
    
        For real problems, the derivative depends also on parameters that do not belong to the state vector (dynamical model
        constants for example). These constants are completely outside of the scope of this interface, the classes that
        implement it are allowed to handle them as they want.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.ODEIntegrator`
              - :class:`~org.hipparchus.ode.FirstOrderConverter`
              - :class:`~org.hipparchus.ode.SecondOrderODE`
    """
    def computeDerivatives(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Get the current time derivative of the state vector.
        
            Parameters:
                t (double): current value of the independent *time* variable
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
    def init(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], double3: float) -> None:
        """
            Initialize equations at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the equations to initialize some internal
            data if needed.
        
            The default implementation does nothing.
        
            Parameters:
                t0 (double): value of the independent *time* variable at integration start
                y0 (double[]): array containing the value of the state vector at integration start
                finalTime (double): target time for the integration
        
        
        """
        ...

class ParameterConfiguration:
    """
    public classParameterConfiguration extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Simple container pairing a parameter name with a step in order to compute the associated Jacobian matrix by finite
        difference.
    
        Instances of this class are guaranteed to be immutable.
    """
    def getHP(self) -> float:
        """
            Get parameter step.
        
            Returns:
                hP parameter step
        
        
        """
        ...
    def getParameterName(self) -> str:
        """
            Get parameter name.
        
            Returns:
                parameterName parameter name
        
        
        """
        ...

class Parameterizable:
    """
    public interfaceParameterizable
    
        This interface enables to process any parameterizable object.
    """
    def getParametersNames(self) -> java.util.List[str]: ...
    def isSupported(self, string: str) -> bool:
        """
            Check if a parameter is supported.
        
            Supported parameters are those listed by :meth:`~org.hipparchus.ode.Parameterizable.getParametersNames`.
        
            Parameters:
                name (:class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): parameter name to check
        
            Returns:
                true if the parameter is supported
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.Parameterizable.getParametersNames`
        
        
        
        """
        ...

class SecondOrderODE:
    """
    public interfaceSecondOrderODE
    
        This interface represents a second order differential equations set.
    
        This interface should be implemented by all real second order differential equation problems before they can be handled
        by the integrators :class:`~org.hipparchus.ode.FirstOrderConverter`.
    
        A second order differential equations problem, as seen by an integrator is the second time derivative :code:`d2Y/dt^2`
        of a state vector :code:`Y`, both being one dimensional arrays. From the integrator point of view, this derivative
        depends only on the current time :code:`t`, on the state vector :code:`Y` and on the first time derivative of the state
        vector.
    
        For real problems, the derivative depends also on parameters that do not belong to the state vector (dynamical model
        constants for example). These constants are completely outside of the scope of this interface, the classes that
        implement it are allowed to handle them as they want.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.FirstOrderConverter`
              - :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`
    """
    def computeSecondDerivatives(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Get the current time derivative of the state vector.
        
            Parameters:
                t (double): current value of the independent *time* variable
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
    public interfaceSecondaryODE
    
        This interface allows users to add secondary differential equations to a primary set of differential equations.
    
        In some cases users may need to integrate some problem-specific equations along with a primary set of differential
        equations. One example is optimal control where adjoined parameters linked to the minimized hamiltonian must be
        integrated.
    
        This interface allows users to add such equations to a primary set of
        :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation` thanks to the
        :meth:`~org.hipparchus.ode.ExpandableODE.addSecondaryEquations` method.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.ExpandableODE`
    """
    def computeDerivatives(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    def getDimension(self) -> int:
        """
            Get the dimension of the secondary state parameters.
        
            Returns:
                dimension of the secondary state parameters
        
        
        """
        ...
    def init(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], double4: float) -> None:
        """
            Initialize equations at the start of an ODE integration.
        
            This method is called once at the start of the integration. It may be used by the equations to initialize some internal
            data if needed.
        
            The default implementation does nothing.
        
            Parameters:
                t0 (double): value of the independent *time* variable at integration start
                primary0 (double[]): array containing the value of the primary state vector at integration start
                secondary0 (double[]): array containing the value of the secondary state vector at integration start
                finalTime (double): target time for the integration
        
        
        """
        ...

class VariationalEquation:
    """
    public classVariationalEquation extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        This class defines a set of :class:`~org.hipparchus.ode.SecondaryODE` to compute the global Jacobian matrices with
        respect to the initial state vector and, if any, to some parameters of the primary ODE set.
    
        The primary set of ODE for which Jaobian matrices are requested may be:
    
          - a full-fledged :class:`~org.hipparchus.ode.ODEJacobiansProvider` that computes by itself both the ODE and its local
            partial derivatives,
          - a simple :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation` which must therefore be completed with a finite
            differences configuration to compute local partial derivatives (so-called internal differentiation).
    
    
        As the variational equation automatically inserts :meth:`~org.hipparchus.ode.ExpandableODE.addSecondaryEquations`, in
        the :class:`~org.hipparchus.ode.ExpandableODE`, data for initial state must also be inserted before integration and
        matrices result must be extracted after integration. This implies a precise scheduling of the calls to the various
        methods of this class. The proper scheduling is the following one:
    
        .. code-block: java
        
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
         
    
        The most important part is to not forget to call :meth:`~org.hipparchus.ode.VariationalEquation.setUpInitialState` to
        add the secondary state with the initial matrices to the :class:`~org.hipparchus.ode.ODEState` used in the
        :meth:`~org.hipparchus.ode.ODEIntegrator.integrate` method. Forgetting to do this and passing only a
        :class:`~org.hipparchus.ode.ODEState` without the secondary state set up will trigger an error as the state vector will
        not have the correct dimension.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.ExpandableODE`
              - :class:`~org.hipparchus.ode.ODEJacobiansProvider`
              - :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.NamedParameterJacobianProvider`
              - :class:`~org.hipparchus.ode.ParametersController`
    """
    @typing.overload
    def __init__(self, expandableODE: ExpandableODE, oDEJacobiansProvider: 'ODEJacobiansProvider'): ...
    @typing.overload
    def __init__(self, expandableODE: ExpandableODE, ordinaryDifferentialEquation: OrdinaryDifferentialEquation, doubleArray: typing.Union[typing.List[float], jpype.JArray], parametersController: 'ParametersController', *parameterConfiguration: ParameterConfiguration): ...
    def extractMainSetJacobian(self, oDEState: ODEState) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Extract the Jacobian matrix with respect to state.
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEState`): state from which to extract Jacobian matrix
        
            Returns:
                Jacobian matrix dY/dY0 with respect to state.
        
        
        """
        ...
    def extractParameterJacobian(self, oDEState: ODEState, string: str) -> typing.MutableSequence[float]:
        """
            Extract the Jacobian matrix with respect to one parameter.
        
            Parameters:
                state (:class:`~org.hipparchus.ode.ODEState`): state from which to extract Jacobian matrix
                pName (:class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): name of the parameter for the computed Jacobian matrix
        
            Returns:
                Jacobian matrix dY/dP with respect to the named parameter
        
        
        """
        ...
    def setInitialMainStateJacobian(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None: ...
    def setInitialParameterJacobian(self, string: str, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    def setUpInitialState(self, oDEState: ODEState) -> ODEState:
        """
            Set up initial state.
        
            This method inserts the initial Jacobian matrices data into an :class:`~org.hipparchus.ode.ODEState` by overriding the
            additional state components corresponding to the instance. It must be called prior to integrate the equations.
        
            This method must be called *after* :meth:`~org.hipparchus.ode.VariationalEquation.setInitialMainStateJacobian` and
            :meth:`~org.hipparchus.ode.VariationalEquation.setInitialParameterJacobian`.
        
            Parameters:
                initialState (:class:`~org.hipparchus.ode.ODEState`): initial state, without the initial Jacobians matrices
        
            Returns:
                a new instance of initial state, with the initial Jacobians matrices properly initialized
        
        
        """
        ...
    class MismatchedEquations(org.hipparchus.exception.MathIllegalArgumentException):
        def __init__(self): ...

_AbstractFieldIntegrator__T = typing.TypeVar('_AbstractFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AbstractFieldIntegrator(FieldODEIntegrator[_AbstractFieldIntegrator__T], typing.Generic[_AbstractFieldIntegrator__T]):
    """
    public abstract classAbstractFieldIntegrator<T extends :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.FieldODEIntegrator`<T>
    
        Base class managing common boilerplate for all integrators.
    """
    def addEventDetector(self, fieldODEEventDetector: org.hipparchus.ode.events.FieldODEEventDetector[_AbstractFieldIntegrator__T]) -> None: ...
    def addStepEndHandler(self, fieldODEStepEndHandler: typing.Union[org.hipparchus.ode.events.FieldODEStepEndHandler[_AbstractFieldIntegrator__T], typing.Callable[['FieldODEStateAndDerivative'[org.hipparchus.CalculusFieldElement], bool], org.hipparchus.ode.events.Action]]) -> None: ...
    def addStepHandler(self, fieldODEStepHandler: typing.Union[org.hipparchus.ode.sampling.FieldODEStepHandler[_AbstractFieldIntegrator__T], typing.Callable[[org.hipparchus.ode.sampling.FieldODEStateInterpolator[org.hipparchus.CalculusFieldElement]], None]]) -> None: ...
    def clearEventDetectors(self) -> None:
        """
            Remove all the event handlers that have been added to the integrator.
        
            Specified by:
                :meth:`~org.hipparchus.ode.FieldODEIntegrator.clearEventDetectors` in
                interface :class:`~org.hipparchus.ode.FieldODEIntegrator`
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.FieldODEIntegrator.addEventDetector`
                  - :meth:`~org.hipparchus.ode.FieldODEIntegrator.getEventDetectors`
        
        
        
        """
        ...
    def clearStepEndHandlers(self) -> None:
        """
            Remove all the handlers for step ends that have been added to the integrator.
        
            Specified by:
                :meth:`~org.hipparchus.ode.FieldODEIntegrator.clearStepEndHandlers` in
                interface :class:`~org.hipparchus.ode.FieldODEIntegrator`
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.FieldODEIntegrator.addStepEndHandler`
                  - :meth:`~org.hipparchus.ode.FieldODEIntegrator.getStepEndHandlers`
        
        
        
        """
        ...
    def clearStepHandlers(self) -> None:
        """
            Remove all the step handlers that have been added to the integrator.
        
            Specified by:
                :meth:`~org.hipparchus.ode.FieldODEIntegrator.clearStepHandlers` in
                interface :class:`~org.hipparchus.ode.FieldODEIntegrator`
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.FieldODEIntegrator.addStepHandler`
                  - :meth:`~org.hipparchus.ode.FieldODEIntegrator.getStepHandlers`
        
        
        
        """
        ...
    def computeDerivatives(self, t: _AbstractFieldIntegrator__T, tArray: typing.Union[typing.List[_AbstractFieldIntegrator__T], jpype.JArray]) -> typing.MutableSequence[_AbstractFieldIntegrator__T]: ...
    def getCurrentSignedStepsize(self) -> _AbstractFieldIntegrator__T:
        """
            Get the current signed value of the integration stepsize.
        
            This method can be called during integration (typically by the object implementing the
            :class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation` problem) if the signed value of the current stepsize that
            is tried is needed.
        
            The result is undefined if the method is called outside of calls to :code:`integrate`.
        
            Specified by:
                :meth:`~org.hipparchus.ode.FieldODEIntegrator.getCurrentSignedStepsize` in
                interface :class:`~org.hipparchus.ode.FieldODEIntegrator`
        
            Returns:
                current signed value of the stepsize
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
            Get the number of evaluations of the differential equations function.
        
            The number of evaluations corresponds to the last call to the :code:`integrate` method. It is 0 if the method has not
            been called yet.
        
            Specified by:
                :meth:`~org.hipparchus.ode.FieldODEIntegrator.getEvaluations` in
                interface :class:`~org.hipparchus.ode.FieldODEIntegrator`
        
            Returns:
                number of evaluations of the differential equations function
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.List[org.hipparchus.ode.events.FieldODEEventDetector[_AbstractFieldIntegrator__T]]: ...
    def getField(self) -> org.hipparchus.Field[_AbstractFieldIntegrator__T]: ...
    def getMaxEvaluations(self) -> int:
        """
            Get the maximal number of functions evaluations.
        
            Specified by:
                :meth:`~org.hipparchus.ode.FieldODEIntegrator.getMaxEvaluations` in
                interface :class:`~org.hipparchus.ode.FieldODEIntegrator`
        
            Returns:
                maximal number of functions evaluations
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the method.
        
            Specified by:
                :meth:`~org.hipparchus.ode.FieldODEIntegrator.getName` in interface :class:`~org.hipparchus.ode.FieldODEIntegrator`
        
            Returns:
                name of the method
        
        
        """
        ...
    def getStepEndHandlers(self) -> java.util.List[org.hipparchus.ode.events.FieldODEStepEndHandler[_AbstractFieldIntegrator__T]]: ...
    def getStepHandlers(self) -> java.util.List[org.hipparchus.ode.sampling.FieldODEStepHandler[_AbstractFieldIntegrator__T]]: ...
    def getStepStart(self) -> 'FieldODEStateAndDerivative'[_AbstractFieldIntegrator__T]: ...
    def setMaxEvaluations(self, int: int) -> None:
        """
            Set the maximal number of differential equations function evaluations.
        
            The purpose of this method is to avoid infinite loops which can occur for example when stringent error constraints are
            set or when lots of discrete events are triggered, thus leading to many rejected steps.
        
            Specified by:
                :meth:`~org.hipparchus.ode.FieldODEIntegrator.setMaxEvaluations` in
                interface :class:`~org.hipparchus.ode.FieldODEIntegrator`
        
            Parameters:
                maxEvaluations (int): maximal number of function evaluations (negative values are silently converted to maximal integer value, thus
                    representing almost unlimited evaluations)
        
        
        """
        ...

class AbstractIntegrator(ODEIntegrator):
    """
    public abstract classAbstractIntegrator extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.ODEIntegrator`
    
        Base class managing common boilerplate for all integrators.
    """
    def addEventDetector(self, oDEEventDetector: org.hipparchus.ode.events.ODEEventDetector) -> None:
        """
            Add an event detector to the integrator.
        
            Specified by:
                :meth:`~org.hipparchus.ode.ODEIntegrator.addEventDetector` in interface :class:`~org.hipparchus.ode.ODEIntegrator`
        
            Parameters:
                detector (:class:`~org.hipparchus.ode.events.ODEEventDetector`): event detector
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.getEventDetectors`
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.clearEventDetectors`
        
        
        
        """
        ...
    def addStepEndHandler(self, oDEStepEndHandler: typing.Union[org.hipparchus.ode.events.ODEStepEndHandler, typing.Callable]) -> None:
        """
            Add a handler for step ends to the integrator.
        
            The :meth:`~org.hipparchus.ode.events.ODEStepEndHandler.stepEndOccurred` method of the :code:`handler` will be called at
            each step end.
        
            Specified by:
                :meth:`~org.hipparchus.ode.ODEIntegrator.addStepEndHandler` in interface :class:`~org.hipparchus.ode.ODEIntegrator`
        
            Parameters:
                handler (:class:`~org.hipparchus.ode.events.ODEStepEndHandler`): handler for step ends
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.getStepEndHandlers`
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.clearStepEndHandlers`
        
        
        
        """
        ...
    def addStepHandler(self, oDEStepHandler: typing.Union[org.hipparchus.ode.sampling.ODEStepHandler, typing.Callable]) -> None:
        """
            Add a step handler to this integrator.
        
            The handler will be called by the integrator for each accepted step.
        
            Specified by:
                :meth:`~org.hipparchus.ode.ODEIntegrator.addStepHandler` in interface :class:`~org.hipparchus.ode.ODEIntegrator`
        
            Parameters:
                handler (:class:`~org.hipparchus.ode.sampling.ODEStepHandler`): handler for the accepted steps
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.getStepHandlers`
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.clearStepHandlers`
        
        
        
        """
        ...
    def clearEventDetectors(self) -> None:
        """
            Remove all the event handlers that have been added to the integrator.
        
            Specified by:
                :meth:`~org.hipparchus.ode.ODEIntegrator.clearEventDetectors` in interface :class:`~org.hipparchus.ode.ODEIntegrator`
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.addEventDetector`
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.getEventDetectors`
        
        
        
        """
        ...
    def clearStepEndHandlers(self) -> None:
        """
            Remove all the handlers for step ends that have been added to the integrator.
        
            Specified by:
                :meth:`~org.hipparchus.ode.ODEIntegrator.clearStepEndHandlers` in interface :class:`~org.hipparchus.ode.ODEIntegrator`
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.addStepEndHandler`
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.getStepEndHandlers`
        
        
        
        """
        ...
    def clearStepHandlers(self) -> None:
        """
            Remove all the step handlers that have been added to the integrator.
        
            Specified by:
                :meth:`~org.hipparchus.ode.ODEIntegrator.clearStepHandlers` in interface :class:`~org.hipparchus.ode.ODEIntegrator`
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.addStepHandler`
                  - :meth:`~org.hipparchus.ode.ODEIntegrator.getStepHandlers`
        
        
        
        """
        ...
    def computeDerivatives(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    def getCurrentSignedStepsize(self) -> float:
        """
            Get the current signed value of the integration stepsize.
        
            This method can be called during integration (typically by the object implementing the
            :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation` problem) if the signed value of the current stepsize that is
            tried is needed.
        
            The result is undefined if the method is called outside of calls to :code:`integrate`.
        
            Specified by:
                :meth:`~org.hipparchus.ode.ODEIntegrator.getCurrentSignedStepsize` in
                interface :class:`~org.hipparchus.ode.ODEIntegrator`
        
            Returns:
                current signed value of the stepsize
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
            Get the number of evaluations of the differential equations function.
        
            The number of evaluations corresponds to the last call to the :code:`integrate` method. It is 0 if the method has not
            been called yet.
        
            Specified by:
                :meth:`~org.hipparchus.ode.ODEIntegrator.getEvaluations` in interface :class:`~org.hipparchus.ode.ODEIntegrator`
        
            Returns:
                number of evaluations of the differential equations function
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.List[org.hipparchus.ode.events.ODEEventDetector]: ...
    def getMaxEvaluations(self) -> int:
        """
            Get the maximal number of functions evaluations.
        
            Specified by:
                :meth:`~org.hipparchus.ode.ODEIntegrator.getMaxEvaluations` in interface :class:`~org.hipparchus.ode.ODEIntegrator`
        
            Returns:
                maximal number of functions evaluations
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the method.
        
            Specified by:
                :meth:`~org.hipparchus.ode.ODEIntegrator.getName` in interface :class:`~org.hipparchus.ode.ODEIntegrator`
        
            Returns:
                name of the method
        
        
        """
        ...
    def getStepEndHandlers(self) -> java.util.List[org.hipparchus.ode.events.ODEStepEndHandler]: ...
    def getStepHandlers(self) -> java.util.List[org.hipparchus.ode.sampling.ODEStepHandler]: ...
    def getStepStart(self) -> 'ODEStateAndDerivative':
        """
            Get the state at step start time t :sub:`i` .
        
            This method can be called during integration (typically by the object implementing the
            :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation` problem) if the value of the current step that is attempted is
            needed.
        
            The result is undefined if the method is called outside of calls to :code:`integrate`.
        
            Specified by:
                :meth:`~org.hipparchus.ode.ODEIntegrator.getStepStart` in interface :class:`~org.hipparchus.ode.ODEIntegrator`
        
            Returns:
                state at step start time t :sub:`i`
        
        
        """
        ...
    def setMaxEvaluations(self, int: int) -> None:
        """
            Set the maximal number of differential equations function evaluations.
        
            The purpose of this method is to avoid infinite loops which can occur for example when stringent error constraints are
            set or when lots of discrete events are triggered, thus leading to many rejected steps.
        
            Specified by:
                :meth:`~org.hipparchus.ode.ODEIntegrator.setMaxEvaluations` in interface :class:`~org.hipparchus.ode.ODEIntegrator`
        
            Parameters:
                maxEvaluations (int): maximal number of function evaluations (negative values are silently converted to maximal integer value, thus
                    representing almost unlimited evaluations)
        
        
        """
        ...

class AbstractParameterizable(Parameterizable):
    """
    public abstract classAbstractParameterizable extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.Parameterizable`
    
        This abstract class provides boilerplate parameters list.
    """
    def complainIfNotSupported(self, string: str) -> None: ...
    def getParametersNames(self) -> java.util.List[str]: ...
    def isSupported(self, string: str) -> bool:
        """
            Check if a parameter is supported.
        
            Supported parameters are those listed by :meth:`~org.hipparchus.ode.Parameterizable.getParametersNames`.
        
            Specified by:
                :meth:`~org.hipparchus.ode.Parameterizable.isSupported` in interface :class:`~org.hipparchus.ode.Parameterizable`
        
            Parameters:
                name (:class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): parameter name to check
        
            Returns:
                true if the parameter is supported
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.Parameterizable.getParametersNames`
        
        
        
        """
        ...

class ComplexODEStateAndDerivative(ComplexODEState):
    """
    public classComplexODEStateAndDerivative extends :class:`~org.hipparchus.ode.ComplexODEState`
    
        Container for time, main and secondary state vectors as well as their derivatives.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.ComplexOrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.ComplexSecondaryODE`
              - :class:`~org.hipparchus.ode.ODEIntegrator`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, complexArray: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], complexArray2: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray]): ...
    @typing.overload
    def __init__(self, double: float, complexArray: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], complexArray2: typing.Union[typing.List[org.hipparchus.complex.Complex], jpype.JArray], complexArray3: typing.Union[typing.List[typing.MutableSequence[org.hipparchus.complex.Complex]], jpype.JArray], complexArray4: typing.Union[typing.List[typing.MutableSequence[org.hipparchus.complex.Complex]], jpype.JArray]): ...
    def getCompleteDerivative(self) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
            Get complete derivative at time.
        
            Returns:
                complete derivative at time, starting with
                :meth:`~org.hipparchus.ode.ComplexODEStateAndDerivative.getPrimaryDerivative`, followed by all
                :meth:`~org.hipparchus.ode.ComplexODEStateAndDerivative.getSecondaryDerivative` in increasing index order
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ComplexODEStateAndDerivative.getPrimaryDerivative`
                  - :meth:`~org.hipparchus.ode.ComplexODEStateAndDerivative.getSecondaryDerivative`
        
        
        
        """
        ...
    def getPrimaryDerivative(self) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
            Get derivative of the primary state at time.
        
            Returns:
                derivative of the primary state at time
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ComplexODEStateAndDerivative.getSecondaryDerivative`
                  - :meth:`~org.hipparchus.ode.ComplexODEStateAndDerivative.getCompleteDerivative`
        
        
        
        """
        ...
    def getSecondaryDerivative(self, int: int) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
            Get derivative of the secondary state at time.
        
            Parameters:
                index (int): index of the secondary set as returned by :meth:`~org.hipparchus.ode.ExpandableODE.addSecondaryEquations` (beware index
                    0 corresponds to primary state, secondary states start at 1)
        
            Returns:
                derivative of the secondary state at time
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ComplexODEStateAndDerivative.getPrimaryDerivative`
                  - :meth:`~org.hipparchus.ode.ComplexODEStateAndDerivative.getCompleteDerivative`
        
        
        
        """
        ...

_FieldODEStateAndDerivative__T = typing.TypeVar('_FieldODEStateAndDerivative__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEStateAndDerivative(FieldODEState[_FieldODEStateAndDerivative__T], typing.Generic[_FieldODEStateAndDerivative__T]):
    """
    public classFieldODEStateAndDerivative<T extends :class:`~org.hipparchus.ode.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.FieldODEState`<T>
    
        Container for time, main and secondary state vectors as well as their derivatives.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.FieldOrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.FieldSecondaryODE`
              - :class:`~org.hipparchus.ode.FieldODEIntegrator`
    """
    @typing.overload
    def __init__(self, t: _FieldODEStateAndDerivative__T, tArray: typing.Union[typing.List[_FieldODEStateAndDerivative__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldODEStateAndDerivative__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, t: _FieldODEStateAndDerivative__T, tArray: typing.Union[typing.List[_FieldODEStateAndDerivative__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldODEStateAndDerivative__T], jpype.JArray], tArray3: typing.Union[typing.List[typing.MutableSequence[_FieldODEStateAndDerivative__T]], jpype.JArray], tArray4: typing.Union[typing.List[typing.MutableSequence[_FieldODEStateAndDerivative__T]], jpype.JArray]): ...
    def getCompleteDerivative(self) -> typing.MutableSequence[_FieldODEStateAndDerivative__T]:
        """
            Get complete derivative at time.
        
            Returns:
                complete derivative at time, starting with :meth:`~org.hipparchus.ode.FieldODEStateAndDerivative.getPrimaryDerivative`,
                followed by all :meth:`~org.hipparchus.ode.FieldODEStateAndDerivative.getSecondaryDerivative` in increasing index order
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.FieldODEStateAndDerivative.getPrimaryDerivative`
                  - :meth:`~org.hipparchus.ode.FieldODEStateAndDerivative.getSecondaryDerivative`
        
        
        
        """
        ...
    def getPrimaryDerivative(self) -> typing.MutableSequence[_FieldODEStateAndDerivative__T]:
        """
            Get derivative of the primary state at time.
        
            Returns:
                derivative of the primary state at time
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.FieldODEStateAndDerivative.getSecondaryDerivative`
                  - :meth:`~org.hipparchus.ode.FieldODEStateAndDerivative.getCompleteDerivative`
        
        
        
        """
        ...
    def getSecondaryDerivative(self, int: int) -> typing.MutableSequence[_FieldODEStateAndDerivative__T]:
        """
            Get derivative of the secondary state at time.
        
            Parameters:
                index (int): index of the secondary set as returned by :meth:`~org.hipparchus.ode.FieldExpandableODE.addSecondaryEquations` (beware
                    index 0 corresponds to primary state, secondary states start at 1)
        
            Returns:
                derivative of the secondary state at time
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.FieldODEStateAndDerivative.getPrimaryDerivative`
                  - :meth:`~org.hipparchus.ode.FieldODEStateAndDerivative.getCompleteDerivative`
        
        
        
        """
        ...

class FirstOrderConverter(OrdinaryDifferentialEquation):
    """
    public classFirstOrderConverter extends :class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`
    
        This class converts second order differential equations to first order ones.
    
        This class is a wrapper around a :class:`~org.hipparchus.ode.SecondOrderODE` which allow to use a
        :class:`~org.hipparchus.ode.ODEIntegrator` to integrate it.
    
        The transformation is done by changing the n dimension state vector to a 2n dimension vector, where the first n
        components are the initial state variables and the n last components are their first time derivative. The first time
        derivative of this state vector then really contains both the first and second time derivative of the initial state
        vector, which can be handled by the underlying second order equations set.
    
        One should be aware that the data is duplicated during the transformation process and that for each call to
        :meth:`~org.hipparchus.ode.FirstOrderConverter.computeDerivatives`, this wrapper does copy 4n scalars : 2n before the
        call to :meth:`~org.hipparchus.ode.SecondOrderODE.computeSecondDerivatives` in order to dispatch the y state vector into
        z and zDot, and 2n after the call to gather zDot and zDDot into yDot. Since the underlying problem by itself perhaps
        also needs to copy data and dispatch the arrays into domain objects, this has an impact on both memory and CPU usage.
        The only way to avoid this duplication is to perform the transformation at the problem level, i.e. to implement the
        problem as a first order one and then avoid using this class.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.ODEIntegrator`
              - :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.SecondOrderODE`
    """
    def __init__(self, secondOrderODE: SecondOrderODE): ...
    def computeDerivatives(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Get the current time derivative of the state vector.
        
            Specified by:
                :meth:`~org.hipparchus.ode.OrdinaryDifferentialEquation.computeDerivatives` in
                interface :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`
        
            Parameters:
                t (double): current value of the independent *time* variable
                y (double[]): array containing the current value of the state vector
        
            Returns:
                time derivative of the state vector
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Get the dimension of the problem.
        
            The dimension of the first order problem is twice the dimension of the underlying second order problem.
        
            Specified by:
                :meth:`~org.hipparchus.ode.OrdinaryDifferentialEquation.getDimension` in
                interface :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`
        
            Returns:
                dimension of the problem
        
        
        """
        ...

class NamedParameterJacobianProvider(Parameterizable):
    """
    public interfaceNamedParameterJacobianProviderextends :class:`~org.hipparchus.ode.Parameterizable`
    
        Interface to compute exactly Jacobian matrix for some parameter when computing
        :class:`~org.hipparchus.ode.VariationalEquation`.
    """
    def computeParameterJacobian(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], string: str) -> typing.MutableSequence[float]: ...

class ODEStateAndDerivative(ODEState):
    """
    public classODEStateAndDerivative extends :class:`~org.hipparchus.ode.ODEState`
    
        Container for time, main and secondary state vectors as well as their derivatives.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`
              - :class:`~org.hipparchus.ode.SecondaryODE`
              - :class:`~org.hipparchus.ode.ODEIntegrator`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], doubleArray3: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray4: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    def getCompleteDerivative(self) -> typing.MutableSequence[float]:
        """
            Get complete derivative at time.
        
            Returns:
                complete derivative at time, starting with :meth:`~org.hipparchus.ode.ODEStateAndDerivative.getPrimaryDerivative`,
                followed by all :meth:`~org.hipparchus.ode.ODEStateAndDerivative.getSecondaryDerivative` in increasing index order
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEStateAndDerivative.getPrimaryDerivative`
                  - :meth:`~org.hipparchus.ode.ODEStateAndDerivative.getSecondaryDerivative`
        
        
        
        """
        ...
    def getPrimaryDerivative(self) -> typing.MutableSequence[float]:
        """
            Get derivative of the primary state at time.
        
            Returns:
                derivative of the primary state at time
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEStateAndDerivative.getSecondaryDerivative`
                  - :meth:`~org.hipparchus.ode.ODEStateAndDerivative.getCompleteDerivative`
        
        
        
        """
        ...
    def getSecondaryDerivative(self, int: int) -> typing.MutableSequence[float]:
        """
            Get derivative of the secondary state at time.
        
            Parameters:
                index (int): index of the secondary set as returned by :meth:`~org.hipparchus.ode.ExpandableODE.addSecondaryEquations` (beware index
                    0 corresponds to primary state, secondary states start at 1)
        
            Returns:
                derivative of the secondary state at time
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.ODEStateAndDerivative.getPrimaryDerivative`
                  - :meth:`~org.hipparchus.ode.ODEStateAndDerivative.getCompleteDerivative`
        
        
        
        """
        ...

class ParametersController(Parameterizable):
    """
    public interfaceParametersControllerextends :class:`~org.hipparchus.ode.Parameterizable`
    
        Interface to compute by finite difference Jacobian matrix for some parameter when computing
        :class:`~org.hipparchus.ode.VariationalEquation`.
    """
    def getParameter(self, string: str) -> float: ...
    def setParameter(self, string: str, double: float) -> None: ...

class ODEJacobiansProvider(OrdinaryDifferentialEquation, NamedParameterJacobianProvider):
    """
    public interfaceODEJacobiansProviderextends :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`, :class:`~org.hipparchus.ode.NamedParameterJacobianProvider`
    
        Interface expanding :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation` in order to compute exactly the Jacobian
        matrices for :class:`~org.hipparchus.ode.VariationalEquation`.
    """
    def computeMainStateJacobian(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    def computeParameterJacobian(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], string: str) -> typing.MutableSequence[float]: ...
    def getParametersNames(self) -> java.util.List[str]: ...
    def isSupported(self, string: str) -> bool:
        """
            Check if a parameter is supported.
        
            Supported parameters are those listed by :meth:`~org.hipparchus.ode.Parameterizable.getParametersNames`.
        
            The default implementation supports no parameters at all.
        
            Specified by:
                :meth:`~org.hipparchus.ode.Parameterizable.isSupported` in interface :class:`~org.hipparchus.ode.Parameterizable`
        
            Parameters:
                name (:class:`~org.hipparchus.ode.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): parameter name to check
        
            Returns:
                true if the parameter is supported
        
            Also see:
        
                  - :meth:`~org.hipparchus.ode.Parameterizable.getParametersNames`
        
        
        
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
