import org.hipparchus
import org.hipparchus.linear
import org.hipparchus.ode
import typing



_AdamsFieldIntegrator__T = typing.TypeVar('_AdamsFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdamsFieldIntegrator(org.hipparchus.ode.MultistepFieldIntegrator[_AdamsFieldIntegrator__T], typing.Generic[_AdamsFieldIntegrator__T]):
    """
    public abstract class AdamsFieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.MultistepFieldIntegrator`<T>
    
        Base class for :class:`~org.hipparchus.ode.nonstiff.AdamsBashforthFieldIntegrator` and
        :class:`~org.hipparchus.ode.nonstiff.AdamsMoultonFieldIntegrator` integrators.
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_AdamsFieldIntegrator__T], string: str, int: int, int2: int, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_AdamsFieldIntegrator__T], string: str, int: int, int2: int, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def integrate(self, fieldExpandableODE: org.hipparchus.ode.FieldExpandableODE[_AdamsFieldIntegrator__T], fieldODEState: org.hipparchus.ode.FieldODEState[_AdamsFieldIntegrator__T], t: _AdamsFieldIntegrator__T) -> org.hipparchus.ode.FieldODEStateAndDerivative[_AdamsFieldIntegrator__T]: ...
    def updateHighOrderDerivativesPhase1(self, array2DRowFieldMatrix: org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsFieldIntegrator__T]) -> org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsFieldIntegrator__T]: ...
    def updateHighOrderDerivativesPhase2(self, tArray: typing.List[_AdamsFieldIntegrator__T], tArray2: typing.List[_AdamsFieldIntegrator__T], array2DRowFieldMatrix: org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsFieldIntegrator__T]) -> None: ...

class AdamsIntegrator(org.hipparchus.ode.MultistepIntegrator):
    """
    public abstract class AdamsIntegrator extends :class:`~org.hipparchus.ode.MultistepIntegrator`
    
        Base class for :class:`~org.hipparchus.ode.nonstiff.AdamsBashforthIntegrator` and
        :class:`~org.hipparchus.ode.nonstiff.AdamsMoultonIntegrator` integrators.
    """
    @typing.overload
    def __init__(self, string: str, int: int, int2: int, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, string: str, int: int, int2: int, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    @typing.overload
    def integrate(self, ordinaryDifferentialEquation: org.hipparchus.ode.OrdinaryDifferentialEquation, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...
    @typing.overload
    def integrate(self, expandableODE: org.hipparchus.ode.ExpandableODE, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...
    def updateHighOrderDerivativesPhase1(self, array2DRowRealMatrix: org.hipparchus.linear.Array2DRowRealMatrix) -> org.hipparchus.linear.Array2DRowRealMatrix:
        """
            Update the high order scaled derivatives for Adams integrators (phase 1).
        
            The complete update of high order derivatives has a form similar to:
        
            .. code-block: java
            
             r :sub:`n+1`  = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1`  u + P :sup:`-1`  A P r :sub:`n` 
             
            this method computes the P :sup:`-1` A P r :sub:`n` part.
        
            Parameters:
                highOrder (Array2DRowRealMatrix): high order scaled derivatives (h :sup:`2` /2 y'', ... h :sup:`k` /k! y(k))
        
            Returns:
                updated high order derivatives
        
            Also see:
        
        
        """
        ...
    def updateHighOrderDerivativesPhase2(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], array2DRowRealMatrix: org.hipparchus.linear.Array2DRowRealMatrix) -> None:
        """
            Update the high order scaled derivatives Adams integrators (phase 2).
        
            The complete update of high order derivatives has a form similar to:
        
            .. code-block: java
            
             r :sub:`n+1`  = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1`  u + P :sup:`-1`  A P r :sub:`n` 
             
            this method computes the (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u part.
        
            Phase 1 of the update must already have been performed.
        
            Parameters:
                start (double[]): first order scaled derivatives at step start
                end (double[]): first order scaled derivatives at step end
                highOrder (Array2DRowRealMatrix): high order scaled derivatives, will be modified (h :sup:`2` /2 y'', ... h :sup:`k` /k! y(k))
        
            Also see:
                :meth:`~org.hipparchus.ode.nonstiff.AdamsIntegrator.updateHighOrderDerivativesPhase1`
        
        
        """
        ...

_AdamsNordsieckFieldTransformer__T = typing.TypeVar('_AdamsNordsieckFieldTransformer__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdamsNordsieckFieldTransformer(typing.Generic[_AdamsNordsieckFieldTransformer__T]):
    """
    public class AdamsNordsieckFieldTransformer<T extends CalculusFieldElement<T>> extends Object
    
        Transformer to Nordsieck vectors for Adams integrators.
    
        This class is used by :class:`~org.hipparchus.ode.nonstiff.AdamsBashforthIntegrator` and
        :class:`~org.hipparchus.ode.nonstiff.AdamsMoultonIntegrator` integrators to convert between classical representation
        with several previous first derivatives and Nordsieck representation with higher order scaled derivatives.
    
        We define scaled derivatives s :sub:`i` (n) at step n as:
    
        .. code-block: java
        
         s :sub:`1` (n) = h y' :sub:`n`  for first derivative
         s :sub:`2` (n) = h :sup:`2` /2 y'' :sub:`n`  for second derivative
         s :sub:`3` (n) = h :sup:`3` /6 y''' :sub:`n`  for third derivative
         ...
         s :sub:`k` (n) = h :sup:`k` /k! y :sup:`(k)`  :sub:`n`  for k :sup:`th`  derivative
         
    
        With the previous definition, the classical representation of multistep methods uses first derivatives only, i.e. it
        handles y :sub:`n` , s :sub:`1` (n) and q :sub:`n` where q :sub:`n` is defined as:
    
        .. code-block: java
        
           q :sub:`n`  = [ s :sub:`1` (n-1) s :sub:`1` (n-2) ... s :sub:`1` (n-(k-1)) ] :sup:`T` 
         
        (we omit the k index in the notation for clarity).
    
        Another possible representation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same
        step, i.e it handles y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as:
    
        .. code-block: java
        
         r :sub:`n`  = [ s :sub:`2` (n), s :sub:`3` (n) ... s :sub:`k` (n) ] :sup:`T` 
         
        (here again we omit the k index in the notation for clarity)
    
        Taylor series formulas show that for any index offset i, s :sub:`1` (n-i) can be computed from s :sub:`1` (n), s
        :sub:`2` (n) ... s :sub:`k` (n), the formula being exact for degree k polynomials.
    
        .. code-block: java
        
         s :sub:`1` (n-i) = s :sub:`1` (n) + ∑ :sub:`j>0`  (j+1) (-i) :sup:`j`  s :sub:`j+1` (n)
         
        The previous formula can be used with several values for i to compute the transform between classical representation and
        Nordsieck vector at step end. The transform between r :sub:`n` and q :sub:`n` resulting from the Taylor series formulas
        above is:
    
        .. code-block: java
        
         q :sub:`n`  = s :sub:`1` (n) u + P r :sub:`n` 
         
        where u is the [ 1 1 ... 1 ] :sup:`T` vector and P is the (k-1)Ã—(k-1) matrix built with the (j+1) (-i) :sup:`j` terms
        with i being the row number starting from 1 and j being the column number starting from 1:
    
        .. code-block: java
        
                [  -2   3   -4    5  ... ]
                [  -4  12  -32   80  ... ]
           P =  [  -6  27 -108  405  ... ]
                [  -8  48 -256 1280  ... ]
                [          ...           ]
         
    
        Changing -i into +i in the formula above can be used to compute a similar transform between classical representation and
        Nordsieck vector at step start. The resulting matrix is simply the absolute value of matrix P.
    
        For :class:`~org.hipparchus.ode.nonstiff.AdamsBashforthIntegrator` method, the Nordsieck vector at step n+1 is computed
        from the Nordsieck vector at step n as follows:
    
          - y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
          - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
          - r :sub:`n+1` = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
        where A is a rows shifting matrix (the lower left part is an identity matrix):
    
        .. code-block: java
        
                [ 0 0   ...  0 0 | 0 ]
                [ ---------------+---]
                [ 1 0   ...  0 0 | 0 ]
            A = [ 0 1   ...  0 0 | 0 ]
                [       ...      | 0 ]
                [ 0 0   ...  1 0 | 0 ]
                [ 0 0   ...  0 1 | 0 ]
         
    
        For :class:`~org.hipparchus.ode.nonstiff.AdamsMoultonIntegrator` method, the predicted Nordsieck vector at step n+1 is
        computed from the Nordsieck vector at step n as follows:
    
          - Y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
          - S :sub:`1` (n+1) = h f(t :sub:`n+1` , Y :sub:`n+1` )
          - R :sub:`n+1` = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
        From this predicted vector, the corrected vector is computed as follows:
    
          - y :sub:`n+1` = y :sub:`n` + S :sub:`1` (n+1) + [ -1 +1 -1 +1 ... ±1 ] r :sub:`n+1`
          - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
          - r :sub:`n+1` = R :sub:`n+1` + (s :sub:`1` (n+1) - S :sub:`1` (n+1)) P :sup:`-1` u
    
        where the upper case Y :sub:`n+1` , S :sub:`1` (n+1) and R :sub:`n+1` represent the predicted states whereas the lower
        case y :sub:`n+1` , s :sub:`n+1` and r :sub:`n+1` represent the corrected states.
    
        We observe that both methods use similar update formulas. In both cases a P :sup:`-1` u vector and a P :sup:`-1` A P
        matrix are used that do not depend on the state, they only depend on k. This class handles these transformations.
    """
    _getInstance__T = typing.TypeVar('_getInstance__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getInstance(field: org.hipparchus.Field[_getInstance__T], int: int) -> 'AdamsNordsieckFieldTransformer'[_getInstance__T]:
        """
            Get the Nordsieck transformer for a given field and number of steps.
        
            Parameters:
                field (Field<T> field): field to which the time and state vector elements belong
                nSteps (int): number of steps of the multistep method (excluding the one being computed)
        
            Returns:
                Nordsieck transformer for the specified field and number of steps
        
        
        """
        ...
    def initializeHighOrderDerivatives(self, t: _AdamsNordsieckFieldTransformer__T, tArray: typing.List[_AdamsNordsieckFieldTransformer__T], tArray2: typing.List[typing.List[_AdamsNordsieckFieldTransformer__T]], tArray3: typing.List[typing.List[_AdamsNordsieckFieldTransformer__T]]) -> org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsNordsieckFieldTransformer__T]: ...
    def updateHighOrderDerivativesPhase1(self, array2DRowFieldMatrix: org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsNordsieckFieldTransformer__T]) -> org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsNordsieckFieldTransformer__T]: ...
    def updateHighOrderDerivativesPhase2(self, tArray: typing.List[_AdamsNordsieckFieldTransformer__T], tArray2: typing.List[_AdamsNordsieckFieldTransformer__T], array2DRowFieldMatrix: org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsNordsieckFieldTransformer__T]) -> None: ...

class AdamsNordsieckTransformer:
    """
    public class AdamsNordsieckTransformer extends Object
    
        Transformer to Nordsieck vectors for Adams integrators.
    
        This class is used by :class:`~org.hipparchus.ode.nonstiff.AdamsBashforthIntegrator` and
        :class:`~org.hipparchus.ode.nonstiff.AdamsMoultonIntegrator` integrators to convert between classical representation
        with several previous first derivatives and Nordsieck representation with higher order scaled derivatives.
    
        We define scaled derivatives s :sub:`i` (n) at step n as:
    
        .. code-block: java
        
         s :sub:`1` (n) = h y' :sub:`n`  for first derivative
         s :sub:`2` (n) = h :sup:`2` /2 y'' :sub:`n`  for second derivative
         s :sub:`3` (n) = h :sup:`3` /6 y''' :sub:`n`  for third derivative
         ...
         s :sub:`k` (n) = h :sup:`k` /k! y :sup:`(k)`  :sub:`n`  for k :sup:`th`  derivative
         
    
        With the previous definition, the classical representation of multistep methods uses first derivatives only, i.e. it
        handles y :sub:`n` , s :sub:`1` (n) and q :sub:`n` where q :sub:`n` is defined as:
    
        .. code-block: java
        
           q :sub:`n`  = [ s :sub:`1` (n-1) s :sub:`1` (n-2) ... s :sub:`1` (n-(k-1)) ] :sup:`T` 
         
        (we omit the k index in the notation for clarity).
    
        Another possible representation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same
        step, i.e it handles y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as:
    
        .. code-block: java
        
         r :sub:`n`  = [ s :sub:`2` (n), s :sub:`3` (n) ... s :sub:`k` (n) ] :sup:`T` 
         
        (here again we omit the k index in the notation for clarity)
    
        Taylor series formulas show that for any index offset i, s :sub:`1` (n-i) can be computed from s :sub:`1` (n), s
        :sub:`2` (n) ... s :sub:`k` (n), the formula being exact for degree k polynomials.
    
        .. code-block: java
        
         s :sub:`1` (n-i) = s :sub:`1` (n) + ∑ :sub:`j>0`  (j+1) (-i) :sup:`j`  s :sub:`j+1` (n)
         
        The previous formula can be used with several values for i to compute the transform between classical representation and
        Nordsieck vector at step end. The transform between r :sub:`n` and q :sub:`n` resulting from the Taylor series formulas
        above is:
    
        .. code-block: java
        
         q :sub:`n`  = s :sub:`1` (n) u + P r :sub:`n` 
         
        where u is the [ 1 1 ... 1 ] :sup:`T` vector and P is the (k-1)Ã—(k-1) matrix built with the (j+1) (-i) :sup:`j` terms
        with i being the row number starting from 1 and j being the column number starting from 1:
    
        .. code-block: java
        
                [  -2   3   -4    5  ... ]
                [  -4  12  -32   80  ... ]
           P =  [  -6  27 -108  405  ... ]
                [  -8  48 -256 1280  ... ]
                [          ...           ]
         
    
        Changing -i into +i in the formula above can be used to compute a similar transform between classical representation and
        Nordsieck vector at step start. The resulting matrix is simply the absolute value of matrix P.
    
        For :class:`~org.hipparchus.ode.nonstiff.AdamsBashforthIntegrator` method, the Nordsieck vector at step n+1 is computed
        from the Nordsieck vector at step n as follows:
    
          - y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
          - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
          - r :sub:`n+1` = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
        where A is a rows shifting matrix (the lower left part is an identity matrix):
    
        .. code-block: java
        
                [ 0 0   ...  0 0 | 0 ]
                [ ---------------+---]
                [ 1 0   ...  0 0 | 0 ]
            A = [ 0 1   ...  0 0 | 0 ]
                [       ...      | 0 ]
                [ 0 0   ...  1 0 | 0 ]
                [ 0 0   ...  0 1 | 0 ]
         
    
        For :class:`~org.hipparchus.ode.nonstiff.AdamsMoultonIntegrator` method, the predicted Nordsieck vector at step n+1 is
        computed from the Nordsieck vector at step n as follows:
    
          - Y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
          - S :sub:`1` (n+1) = h f(t :sub:`n+1` , Y :sub:`n+1` )
          - R :sub:`n+1` = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
        From this predicted vector, the corrected vector is computed as follows:
    
          - y :sub:`n+1` = y :sub:`n` + S :sub:`1` (n+1) + [ -1 +1 -1 +1 ... ±1 ] r :sub:`n+1`
          - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
          - r :sub:`n+1` = R :sub:`n+1` + (s :sub:`1` (n+1) - S :sub:`1` (n+1)) P :sup:`-1` u
    
        where the upper case Y :sub:`n+1` , S :sub:`1` (n+1) and R :sub:`n+1` represent the predicted states whereas the lower
        case y :sub:`n+1` , s :sub:`n+1` and r :sub:`n+1` represent the corrected states.
    
        We observe that both methods use similar update formulas. In both cases a P :sup:`-1` u vector and a P :sup:`-1` A P
        matrix are used that do not depend on the state, they only depend on k. This class handles these transformations.
    """
    @staticmethod
    def getInstance(int: int) -> 'AdamsNordsieckTransformer':
        """
            Get the Nordsieck transformer for a given number of steps.
        
            Parameters:
                nSteps (int): number of steps of the multistep method (excluding the one being computed)
        
            Returns:
                Nordsieck transformer for the specified number of steps
        
        
        """
        ...
    def initializeHighOrderDerivatives(self, double: float, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]], doubleArray3: typing.List[typing.List[float]]) -> org.hipparchus.linear.Array2DRowRealMatrix:
        """
            Initialize the high order scaled derivatives at step start.
        
            Parameters:
                h (double): step size to use for scaling
                t (double[]): first steps times
                y (double[][]): first steps states
                yDot (double[][]): first steps derivatives
        
            Returns:
                Nordieck vector at start of first step (h :sup:`2` /2 y'' :sub:`n` , h :sup:`3` /6 y''' :sub:`n` ... h :sup:`k` /k! y
                :sup:`(k)` :sub:`n` )
        
        
        """
        ...
    def updateHighOrderDerivativesPhase1(self, array2DRowRealMatrix: org.hipparchus.linear.Array2DRowRealMatrix) -> org.hipparchus.linear.Array2DRowRealMatrix:
        """
            Update the high order scaled derivatives for Adams integrators (phase 1).
        
            The complete update of high order derivatives has a form similar to:
        
            .. code-block: java
            
             r :sub:`n+1`  = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1`  u + P :sup:`-1`  A P r :sub:`n` 
             
            this method computes the P :sup:`-1` A P r :sub:`n` part.
        
            Parameters:
                highOrder (Array2DRowRealMatrix): high order scaled derivatives (h :sup:`2` /2 y'', ... h :sup:`k` /k! y(k))
        
            Returns:
                updated high order derivatives
        
            Also see:
        
        
        """
        ...
    def updateHighOrderDerivativesPhase2(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], array2DRowRealMatrix: org.hipparchus.linear.Array2DRowRealMatrix) -> None:
        """
            Update the high order scaled derivatives Adams integrators (phase 2).
        
            The complete update of high order derivatives has a form similar to:
        
            .. code-block: java
            
             r :sub:`n+1`  = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1`  u + P :sup:`-1`  A P r :sub:`n` 
             
            this method computes the (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u part.
        
            Phase 1 of the update must already have been performed.
        
            Parameters:
                start (double[]): first order scaled derivatives at step start
                end (double[]): first order scaled derivatives at step end
                highOrder (Array2DRowRealMatrix): high order scaled derivatives, will be modified (h :sup:`2` /2 y'', ... h :sup:`k` /k! y(k))
        
            Also see:
                :meth:`~org.hipparchus.ode.nonstiff.AdamsNordsieckTransformer.updateHighOrderDerivativesPhase1`
        
        
        """
        ...

_AdaptiveStepsizeFieldIntegrator__T = typing.TypeVar('_AdaptiveStepsizeFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdaptiveStepsizeFieldIntegrator(org.hipparchus.ode.AbstractFieldIntegrator[_AdaptiveStepsizeFieldIntegrator__T], typing.Generic[_AdaptiveStepsizeFieldIntegrator__T]):
    """
    public abstract class AdaptiveStepsizeFieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.AbstractFieldIntegrator`<T>
    
        This abstract class holds the common part of all adaptive stepsize integrators for Ordinary Differential Equations.
    
        These algorithms perform integration with stepsize control, which means the user does not specify the integration step
        but rather a tolerance on error. The error threshold is computed as
    
        .. code-block: java
        
         threshold_i = absTol_i + relTol_i * max (abs (ym), abs (ym+1))
         
        where absTol_i is the absolute tolerance for component i of the state vector and relTol_i is the relative tolerance for
        the same component. The user can also use only two scalar values absTol and relTol which will be used for all
        components.
    
        Note that *only* the :meth:`~org.hipparchus.ode.FieldODEState.getPrimaryState` of the state vector is used for stepsize
        control. The :meth:`~org.hipparchus.ode.FieldODEState.getSecondaryState` of the state vector are explicitly ignored for
        stepsize control.
    
        If the estimated error for ym+1 is such that
    
        .. code-block: java
        
         sqrt((sum (errEst_i / threshold_i)^2 ) / n) < 1
         
        (where n is the main set dimension) then the step is accepted, otherwise the step is rejected and a new attempt is made
        with a new stepsize.
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_AdaptiveStepsizeFieldIntegrator__T], string: str, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_AdaptiveStepsizeFieldIntegrator__T], string: str, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def getMaxStep(self) -> float:
        """
            Get the maximal step.
        
            Returns:
                maximal step
        
        
        """
        ...
    def getMinStep(self) -> float:
        """
            Get the minimal step.
        
            Returns:
                minimal step
        
        
        """
        ...
    def initializeStep(self, boolean: bool, int: int, tArray: typing.List[_AdaptiveStepsizeFieldIntegrator__T], fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_AdaptiveStepsizeFieldIntegrator__T], fieldEquationsMapper: org.hipparchus.ode.FieldEquationsMapper[_AdaptiveStepsizeFieldIntegrator__T]) -> float: ...
    def setInitialStepSize(self, double: float) -> None:
        """
            Set the initial step size.
        
            This method allows the user to specify an initial positive step size instead of letting the integrator guess it by
            itself. If this method is not called before integration is started, the initial step size will be estimated by the
            integrator.
        
            Parameters:
                initialStepSize (double): initial step size to use (must be positive even for backward integration ; providing a negative value or a value outside
                    of the min/max step interval will lead the integrator to ignore the value and compute the initial step size by itself)
        
        
        """
        ...
    @typing.overload
    def setStepSizeControl(self, double: float, double2: float, double3: float, double4: float) -> None:
        """
            Set the adaptive step size control parameters.
        
            A side effect of this method is to also reset the initial step so it will be automatically computed by the integrator if
            :meth:`~org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator.setInitialStepSize` is not called by the user.
        
            Parameters:
                minimalStep (double): minimal step (must be positive even for backward integration), the last step can be smaller than this
                maximalStep (double): maximal step (must be positive even for backward integration)
                absoluteTolerance (double): allowed absolute error
                relativeTolerance (double): allowed relative error
        
            Set the adaptive step size control parameters.
        
            A side effect of this method is to also reset the initial step so it will be automatically computed by the integrator if
            :meth:`~org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator.setInitialStepSize` is not called by the user.
        
            Parameters:
                minimalStep (double): minimal step (must be positive even for backward integration), the last step can be smaller than this
                maximalStep (double): maximal step (must be positive even for backward integration)
                absoluteTolerance (double[]): allowed absolute error
                relativeTolerance (double[]): allowed relative error
        
        
        """
        ...
    @typing.overload
    def setStepSizeControl(self, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> None: ...

class AdaptiveStepsizeIntegrator(org.hipparchus.ode.AbstractIntegrator):
    """
    public abstract class AdaptiveStepsizeIntegrator extends :class:`~org.hipparchus.ode.AbstractIntegrator`
    
        This abstract class holds the common part of all adaptive stepsize integrators for Ordinary Differential Equations.
    
        These algorithms perform integration with stepsize control, which means the user does not specify the integration step
        but rather a tolerance on error. The error threshold is computed as
    
        .. code-block: java
        
         threshold_i = absTol_i + relTol_i * max (abs (ym), abs (ym+1))
         
        where absTol_i is the absolute tolerance for component i of the state vector and relTol_i is the relative tolerance for
        the same component. The user can also use only two scalar values absTol and relTol which will be used for all
        components.
    
        If the Ordinary Differential Equations is an :class:`~org.hipparchus.ode.ExpandableODE` rather than a
        :class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`, then *only* the
        :meth:`~org.hipparchus.ode.ExpandableODE.getPrimary` of the state vector is used for stepsize control, not the complete
        state vector.
    
        If the estimated error for ym+1 is such that
    
        .. code-block: java
        
         sqrt((sum (errEst_i / threshold_i)^2 ) / n) < 1
         
        (where n is the main set dimension) then the step is accepted, otherwise the step is rejected and a new attempt is made
        with a new stepsize.
    """
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def getMaxStep(self) -> float:
        """
            Get the maximal step.
        
            Returns:
                maximal step
        
        
        """
        ...
    def getMinStep(self) -> float:
        """
            Get the minimal step.
        
            Returns:
                minimal step
        
        
        """
        ...
    def initializeStep(self, boolean: bool, int: int, doubleArray: typing.List[float], oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, equationsMapper: org.hipparchus.ode.EquationsMapper) -> float: ...
    def setInitialStepSize(self, double: float) -> None:
        """
            Set the initial step size.
        
            This method allows the user to specify an initial positive step size instead of letting the integrator guess it by
            itself. If this method is not called before integration is started, the initial step size will be estimated by the
            integrator.
        
            Parameters:
                initialStepSize (double): initial step size to use (must be positive even for backward integration ; providing a negative value or a value outside
                    of the min/max step interval will lead the integrator to ignore the value and compute the initial step size by itself)
        
        
        """
        ...
    @typing.overload
    def setStepSizeControl(self, double: float, double2: float, double3: float, double4: float) -> None:
        """
            Set the adaptive step size control parameters.
        
            A side effect of this method is to also reset the initial step so it will be automatically computed by the integrator if
            :meth:`~org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator.setInitialStepSize` is not called by the user.
        
            Parameters:
                minimalStep (double): minimal step (must be positive even for backward integration), the last step can be smaller than this
                maximalStep (double): maximal step (must be positive even for backward integration)
                absoluteTolerance (double): allowed absolute error
                relativeTolerance (double): allowed relative error
        
            Set the adaptive step size control parameters.
        
            A side effect of this method is to also reset the initial step so it will be automatically computed by the integrator if
            :meth:`~org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator.setInitialStepSize` is not called by the user.
        
            Parameters:
                minimalStep (double): minimal step (must be positive even for backward integration), the last step can be smaller than this
                maximalStep (double): maximal step (must be positive even for backward integration)
                absoluteTolerance (double[]): allowed absolute error
                relativeTolerance (double[]): allowed relative error
        
        
        """
        ...
    @typing.overload
    def setStepSizeControl(self, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> None: ...

class ButcherArrayProvider:
    """
    public interface ButcherArrayProvider
    
        This interface represents an integrator based on Butcher arrays.
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.RungeKuttaIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaIntegrator`
    """
    def getA(self) -> typing.List[typing.List[float]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[float]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[float]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...

_FieldButcherArrayProvider__T = typing.TypeVar('_FieldButcherArrayProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldButcherArrayProvider(typing.Generic[_FieldButcherArrayProvider__T]):
    """
    public interface FieldButcherArrayProvider<T extends CalculusFieldElement<T>>
    
        This interface represents an integrator based on Butcher arrays.
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.RungeKuttaFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator`
    """
    def getA(self) -> typing.List[typing.List[_FieldButcherArrayProvider__T]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[_FieldButcherArrayProvider__T]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[_FieldButcherArrayProvider__T]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...

class StepsizeHelper:
    """
    public class StepsizeHelper extends Object
    
        Helper for adaptive stepsize control.
    
        Since:
            2.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    _filterStep_1__T = typing.TypeVar('_filterStep_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def filterStep(self, double: float, boolean: bool, boolean2: bool) -> float: ...
    @typing.overload
    def filterStep(self, t: _filterStep_1__T, boolean: bool, boolean2: bool) -> _filterStep_1__T: ...
    def getDummyStepsize(self) -> float:
        """
            Get a dummy step size.
        
            Returns:
                geometric mean of :meth:`~org.hipparchus.ode.nonstiff.StepsizeHelper.getMinStep` and
                :meth:`~org.hipparchus.ode.nonstiff.StepsizeHelper.getMaxStep`
        
        
        """
        ...
    def getInitialStep(self) -> float:
        """
            Get the initial step.
        
            Returns:
                initial step
        
        
        """
        ...
    def getMainSetDimension(self) -> int:
        """
            Get the main set dimension.
        
            Returns:
                main set dimension
        
        
        """
        ...
    def getMaxStep(self) -> float:
        """
            Get the maximal step.
        
            Returns:
                maximal step
        
        
        """
        ...
    def getMinStep(self) -> float:
        """
            Get the minimal step.
        
            Returns:
                minimal step
        
        
        """
        ...
    def getRelativeTolerance(self, int: int) -> float:
        """
            Get the relative tolerance for one component.
        
            Parameters:
                i (int): component to select
        
            Returns:
                relative tolerance for selected component
        
        
        """
        ...
    _getTolerance_1__T = typing.TypeVar('_getTolerance_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTolerance(self, int: int, double: float) -> float:
        """
            Get the tolerance for one component.
        
            Parameters:
                i (int): component to select
                scale (double): scale factor for relative tolerance (i.e. y[i])
        
            Returns:
                tolerance for selected component
        
        """
        ...
    @typing.overload
    def getTolerance(self, int: int, t: _getTolerance_1__T) -> _getTolerance_1__T:
        """
            Get the tolerance for one component.
        
            Parameters:
                i (int): component to select
                scale (T): scale factor for relative tolerance (i.e. y[i])
        
            Returns:
                tolerance for selected component
        
        
        """
        ...
    def setInitialStepSize(self, double: float) -> None:
        """
            Set the initial step size.
        
            This method allows the user to specify an initial positive step size instead of letting the integrator guess it by
            itself. If this method is not called before integration is started, the initial step size will be estimated by the
            integrator.
        
            Parameters:
                initialStepSize (double): initial step size to use (must be positive even for backward integration ; providing a negative value or a value outside
                    of the min/max step interval will lead the integrator to ignore the value and compute the initial step size by itself)
        
        
        """
        ...

_AdamsBashforthFieldIntegrator__T = typing.TypeVar('_AdamsBashforthFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdamsBashforthFieldIntegrator(AdamsFieldIntegrator[_AdamsBashforthFieldIntegrator__T], typing.Generic[_AdamsBashforthFieldIntegrator__T]):
    """
    public class AdamsBashforthFieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.nonstiff.AdamsFieldIntegrator`<T>
    
        This class implements explicit Adams-Bashforth integrators for Ordinary Differential Equations.
    
        Adams-Bashforth methods (in fact due to Adams alone) are explicit multistep ODE solvers. This implementation is a
        variation of the classical one: it uses adaptive stepsize to implement error control, whereas classical implementations
        are fixed step size. The value of state vector at step n+1 is a simple combination of the value at step n and of the
        derivatives at steps n, n-1, n-2 ... Depending on the number k of previous steps one wants to use for computing the next
        value, different formulas are available:
    
          - k = 1: y :sub:`n+1` = y :sub:`n` + h y' :sub:`n`
          - k = 2: y :sub:`n+1` = y :sub:`n` + h (3y' :sub:`n` -y' :sub:`n-1` )/2
          - k = 3: y :sub:`n+1` = y :sub:`n` + h (23y' :sub:`n` -16y' :sub:`n-1` +5y' :sub:`n-2` )/12
          - k = 4: y :sub:`n+1` = y :sub:`n` + h (55y' :sub:`n` -59y' :sub:`n-1` +37y' :sub:`n-2` -9y' :sub:`n-3` )/24
          - ...
    
    
        A k-steps Adams-Bashforth method is of order k.
    
        There must be sufficient time for the :meth:`~org.hipparchus.ode.MultistepFieldIntegrator.setStarterIntegrator` to take
        several steps between the the last reset event, and the end of integration, otherwise an exception may be thrown during
        integration. The user can adjust the end date of integration, or the step size of the starter integrator to ensure a
        sufficient number of steps can be completed before the end of integration.
    
        Implementation details
    ----------------------
    
    
        We define scaled derivatives s :sub:`i` (n) at step n as:
    
        .. code-block: java
        
         s :sub:`1` (n) = h y' :sub:`n`  for first derivative
         s :sub:`2` (n) = h :sup:`2` /2 y'' :sub:`n`  for second derivative
         s :sub:`3` (n) = h :sup:`3` /6 y''' :sub:`n`  for third derivative
         ...
         s :sub:`k` (n) = h :sup:`k` /k! y :sup:`(k)`  :sub:`n`  for k :sup:`th`  derivative
         
    
        The definitions above use the classical representation with several previous first derivatives. Lets define
    
        .. code-block: java
        
           q :sub:`n`  = [ s :sub:`1` (n-1) s :sub:`1` (n-2) ... s :sub:`1` (n-(k-1)) ] :sup:`T` 
         
        (we omit the k index in the notation for clarity). With these definitions, Adams-Bashforth methods can be written:
    
          - k = 1: y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n)
          - k = 2: y :sub:`n+1` = y :sub:`n` + 3/2 s :sub:`1` (n) + [ -1/2 ] q :sub:`n`
          - k = 3: y :sub:`n+1` = y :sub:`n` + 23/12 s :sub:`1` (n) + [ -16/12 5/12 ] q :sub:`n`
          - k = 4: y :sub:`n+1` = y :sub:`n` + 55/24 s :sub:`1` (n) + [ -59/24 37/24 -9/24 ] q :sub:`n`
          - ...
    
    
        Instead of using the classical representation with first derivatives only (y :sub:`n` , s :sub:`1` (n) and q :sub:`n` ),
        our implementation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same step (y
        :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as:
    
        .. code-block: java
        
         r :sub:`n`  = [ s :sub:`2` (n), s :sub:`3` (n) ... s :sub:`k` (n) ] :sup:`T` 
         
        (here again we omit the k index in the notation for clarity)
    
        Taylor series formulas show that for any index offset i, s :sub:`1` (n-i) can be computed from s :sub:`1` (n), s
        :sub:`2` (n) ... s :sub:`k` (n), the formula being exact for degree k polynomials.
    
        .. code-block: java
        
         s :sub:`1` (n-i) = s :sub:`1` (n) + ∑ :sub:`j>0`  (j+1) (-i) :sup:`j`  s :sub:`j+1` (n)
         
        The previous formula can be used with several values for i to compute the transform between classical representation and
        Nordsieck vector. The transform between r :sub:`n` and q :sub:`n` resulting from the Taylor series formulas above is:
    
        .. code-block: java
        
         q :sub:`n`  = s :sub:`1` (n) u + P r :sub:`n` 
         
        where u is the [ 1 1 ... 1 ] :sup:`T` vector and P is the (k-1)Ã—(k-1) matrix built with the (j+1) (-i) :sup:`j` terms
        with i being the row number starting from 1 and j being the column number starting from 1:
    
        .. code-block: java
        
                [  -2   3   -4    5  ... ]
                [  -4  12  -32   80  ... ]
           P =  [  -6  27 -108  405  ... ]
                [  -8  48 -256 1280  ... ]
                [          ...           ]
         
    
        Using the Nordsieck vector has several advantages:
    
          - it greatly simplifies step interpolation as the interpolator mainly applies Taylor series formulas,
          - it simplifies step changes that occur when discrete events that truncate the step are triggered,
          - it allows to extend the methods in order to support adaptive stepsize.
    
    
        The Nordsieck vector at step n+1 is computed from the Nordsieck vector at step n as follows:
    
          - y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
          - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
          - r :sub:`n+1` = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
        where A is a rows shifting matrix (the lower left part is an identity matrix):
    
        .. code-block: java
        
                [ 0 0   ...  0 0 | 0 ]
                [ ---------------+---]
                [ 1 0   ...  0 0 | 0 ]
            A = [ 0 1   ...  0 0 | 0 ]
                [       ...      | 0 ]
                [ 0 0   ...  1 0 | 0 ]
                [ 0 0   ...  0 1 | 0 ]
         
    
        The P :sup:`-1` u vector and the P :sup:`-1` A P matrix do not depend on the state, they only depend on k and therefore
        are precomputed once for all.
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_AdamsBashforthFieldIntegrator__T], int: int, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_AdamsBashforthFieldIntegrator__T], int: int, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...

class AdamsBashforthIntegrator(AdamsIntegrator):
    """
    public class AdamsBashforthIntegrator extends :class:`~org.hipparchus.ode.nonstiff.AdamsIntegrator`
    
        This class implements explicit Adams-Bashforth integrators for Ordinary Differential Equations.
    
        Adams-Bashforth methods (in fact due to Adams alone) are explicit multistep ODE solvers. This implementation is a
        variation of the classical one: it uses adaptive stepsize to implement error control, whereas classical implementations
        are fixed step size. The value of state vector at step n+1 is a simple combination of the value at step n and of the
        derivatives at steps n, n-1, n-2 ... Depending on the number k of previous steps one wants to use for computing the next
        value, different formulas are available:
    
          - k = 1: y :sub:`n+1` = y :sub:`n` + h y' :sub:`n`
          - k = 2: y :sub:`n+1` = y :sub:`n` + h (3y' :sub:`n` -y' :sub:`n-1` )/2
          - k = 3: y :sub:`n+1` = y :sub:`n` + h (23y' :sub:`n` -16y' :sub:`n-1` +5y' :sub:`n-2` )/12
          - k = 4: y :sub:`n+1` = y :sub:`n` + h (55y' :sub:`n` -59y' :sub:`n-1` +37y' :sub:`n-2` -9y' :sub:`n-3` )/24
          - ...
    
    
        A k-steps Adams-Bashforth method is of order k.
    
        There must be sufficient time for the :meth:`~org.hipparchus.ode.MultistepIntegrator.setStarterIntegrator` to take
        several steps between the the last reset event, and the end of integration, otherwise an exception may be thrown during
        integration. The user can adjust the end date of integration, or the step size of the starter integrator to ensure a
        sufficient number of steps can be completed before the end of integration.
    
        Implementation details
    ----------------------
    
    
        We define scaled derivatives s :sub:`i` (n) at step n as:
    
        .. code-block: java
        
         s :sub:`1` (n) = h y' :sub:`n`  for first derivative
         s :sub:`2` (n) = h :sup:`2` /2 y'' :sub:`n`  for second derivative
         s :sub:`3` (n) = h :sup:`3` /6 y''' :sub:`n`  for third derivative
         ...
         s :sub:`k` (n) = h :sup:`k` /k! y :sup:`(k)`  :sub:`n`  for k :sup:`th`  derivative
         
    
        The definitions above use the classical representation with several previous first derivatives. Lets define
    
        .. code-block: java
        
           q :sub:`n`  = [ s :sub:`1` (n-1) s :sub:`1` (n-2) ... s :sub:`1` (n-(k-1)) ] :sup:`T` 
         
        (we omit the k index in the notation for clarity). With these definitions, Adams-Bashforth methods can be written:
    
          - k = 1: y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n)
          - k = 2: y :sub:`n+1` = y :sub:`n` + 3/2 s :sub:`1` (n) + [ -1/2 ] q :sub:`n`
          - k = 3: y :sub:`n+1` = y :sub:`n` + 23/12 s :sub:`1` (n) + [ -16/12 5/12 ] q :sub:`n`
          - k = 4: y :sub:`n+1` = y :sub:`n` + 55/24 s :sub:`1` (n) + [ -59/24 37/24 -9/24 ] q :sub:`n`
          - ...
    
    
        Instead of using the classical representation with first derivatives only (y :sub:`n` , s :sub:`1` (n) and q :sub:`n` ),
        our implementation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same step (y
        :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as:
    
        .. code-block: java
        
         r :sub:`n`  = [ s :sub:`2` (n), s :sub:`3` (n) ... s :sub:`k` (n) ] :sup:`T` 
         
        (here again we omit the k index in the notation for clarity)
    
        Taylor series formulas show that for any index offset i, s :sub:`1` (n-i) can be computed from s :sub:`1` (n), s
        :sub:`2` (n) ... s :sub:`k` (n), the formula being exact for degree k polynomials.
    
        .. code-block: java
        
         s :sub:`1` (n-i) = s :sub:`1` (n) + ∑ :sub:`j>0`  (j+1) (-i) :sup:`j`  s :sub:`j+1` (n)
         
        The previous formula can be used with several values for i to compute the transform between classical representation and
        Nordsieck vector. The transform between r :sub:`n` and q :sub:`n` resulting from the Taylor series formulas above is:
    
        .. code-block: java
        
         q :sub:`n`  = s :sub:`1` (n) u + P r :sub:`n` 
         
        where u is the [ 1 1 ... 1 ] :sup:`T` vector and P is the (k-1)Ã—(k-1) matrix built with the (j+1) (-i) :sup:`j` terms
        with i being the row number starting from 1 and j being the column number starting from 1:
    
        .. code-block: java
        
                [  -2   3   -4    5  ... ]
                [  -4  12  -32   80  ... ]
           P =  [  -6  27 -108  405  ... ]
                [  -8  48 -256 1280  ... ]
                [          ...           ]
         
    
        Using the Nordsieck vector has several advantages:
    
          - it greatly simplifies step interpolation as the interpolator mainly applies Taylor series formulas,
          - it simplifies step changes that occur when discrete events that truncate the step are triggered,
          - it allows to extend the methods in order to support adaptive stepsize.
    
    
        The Nordsieck vector at step n+1 is computed from the Nordsieck vector at step n as follows:
    
          - y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
          - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
          - r :sub:`n+1` = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
        where A is a rows shifting matrix (the lower left part is an identity matrix):
    
        .. code-block: java
        
                [ 0 0   ...  0 0 | 0 ]
                [ ---------------+---]
                [ 1 0   ...  0 0 | 0 ]
            A = [ 0 1   ...  0 0 | 0 ]
                [       ...      | 0 ]
                [ 0 0   ...  1 0 | 0 ]
                [ 0 0   ...  0 1 | 0 ]
         
    
        The P :sup:`-1` u vector and the P :sup:`-1` A P matrix do not depend on the state, they only depend on k and therefore
        are precomputed once for all.
    """
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...

_AdamsMoultonFieldIntegrator__T = typing.TypeVar('_AdamsMoultonFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdamsMoultonFieldIntegrator(AdamsFieldIntegrator[_AdamsMoultonFieldIntegrator__T], typing.Generic[_AdamsMoultonFieldIntegrator__T]):
    """
    public class AdamsMoultonFieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.nonstiff.AdamsFieldIntegrator`<T>
    
        This class implements implicit Adams-Moulton integrators for Ordinary Differential Equations.
    
        Adams-Moulton methods (in fact due to Adams alone) are implicit multistep ODE solvers. This implementation is a
        variation of the classical one: it uses adaptive stepsize to implement error control, whereas classical implementations
        are fixed step size. The value of state vector at step n+1 is a simple combination of the value at step n and of the
        derivatives at steps n+1, n, n-1 ... Since y' :sub:`n+1` is needed to compute y :sub:`n+1` , another method must be used
        to compute a first estimate of y :sub:`n+1` , then compute y' :sub:`n+1` , then compute a final estimate of y :sub:`n+1`
        using the following formulas. Depending on the number k of previous steps one wants to use for computing the next value,
        different formulas are available for the final estimate:
    
          - k = 1: y :sub:`n+1` = y :sub:`n` + h y' :sub:`n+1`
          - k = 2: y :sub:`n+1` = y :sub:`n` + h (y' :sub:`n+1` +y' :sub:`n` )/2
          - k = 3: y :sub:`n+1` = y :sub:`n` + h (5y' :sub:`n+1` +8y' :sub:`n` -y' :sub:`n-1` )/12
          - k = 4: y :sub:`n+1` = y :sub:`n` + h (9y' :sub:`n+1` +19y' :sub:`n` -5y' :sub:`n-1` +y' :sub:`n-2` )/24
          - ...
    
    
        A k-steps Adams-Moulton method is of order k+1.
    
        There must be sufficient time for the :meth:`~org.hipparchus.ode.MultistepFieldIntegrator.setStarterIntegrator` to take
        several steps between the the last reset event, and the end of integration, otherwise an exception may be thrown during
        integration. The user can adjust the end date of integration, or the step size of the starter integrator to ensure a
        sufficient number of steps can be completed before the end of integration.
    
        Implementation details
    ----------------------
    
    
        We define scaled derivatives s :sub:`i` (n) at step n as:
    
        .. code-block: java
        
         s :sub:`1` (n) = h y' :sub:`n`  for first derivative
         s :sub:`2` (n) = h :sup:`2` /2 y'' :sub:`n`  for second derivative
         s :sub:`3` (n) = h :sup:`3` /6 y''' :sub:`n`  for third derivative
         ...
         s :sub:`k` (n) = h :sup:`k` /k! y :sup:`(k)`  :sub:`n`  for k :sup:`th`  derivative
         
    
        The definitions above use the classical representation with several previous first derivatives. Lets define
    
        .. code-block: java
        
           q :sub:`n`  = [ s :sub:`1` (n-1) s :sub:`1` (n-2) ... s :sub:`1` (n-(k-1)) ] :sup:`T` 
         
        (we omit the k index in the notation for clarity). With these definitions, Adams-Moulton methods can be written:
    
          - k = 1: y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n+1)
          - k = 2: y :sub:`n+1` = y :sub:`n` + 1/2 s :sub:`1` (n+1) + [ 1/2 ] q :sub:`n+1`
          - k = 3: y :sub:`n+1` = y :sub:`n` + 5/12 s :sub:`1` (n+1) + [ 8/12 -1/12 ] q :sub:`n+1`
          - k = 4: y :sub:`n+1` = y :sub:`n` + 9/24 s :sub:`1` (n+1) + [ 19/24 -5/24 1/24 ] q :sub:`n+1`
          - ...
    
    
        Instead of using the classical representation with first derivatives only (y :sub:`n` , s :sub:`1` (n+1) and q
        :sub:`n+1` ), our implementation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same
        step (y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as:
    
        .. code-block: java
        
         r :sub:`n`  = [ s :sub:`2` (n), s :sub:`3` (n) ... s :sub:`k` (n) ] :sup:`T` 
         
        (here again we omit the k index in the notation for clarity)
    
        Taylor series formulas show that for any index offset i, s :sub:`1` (n-i) can be computed from s :sub:`1` (n), s
        :sub:`2` (n) ... s :sub:`k` (n), the formula being exact for degree k polynomials.
    
        .. code-block: java
        
         s :sub:`1` (n-i) = s :sub:`1` (n) + ∑ :sub:`j>0`  (j+1) (-i) :sup:`j`  s :sub:`j+1` (n)
         
        The previous formula can be used with several values for i to compute the transform between classical representation and
        Nordsieck vector. The transform between r :sub:`n` and q :sub:`n` resulting from the Taylor series formulas above is:
    
        .. code-block: java
        
         q :sub:`n`  = s :sub:`1` (n) u + P r :sub:`n` 
         
        where u is the [ 1 1 ... 1 ] :sup:`T` vector and P is the (k-1)Ã—(k-1) matrix built with the (j+1) (-i) :sup:`j` terms
        with i being the row number starting from 1 and j being the column number starting from 1:
    
        .. code-block: java
        
                [  -2   3   -4    5  ... ]
                [  -4  12  -32   80  ... ]
           P =  [  -6  27 -108  405  ... ]
                [  -8  48 -256 1280  ... ]
                [          ...           ]
         
    
        Using the Nordsieck vector has several advantages:
    
          - it greatly simplifies step interpolation as the interpolator mainly applies Taylor series formulas,
          - it simplifies step changes that occur when discrete events that truncate the step are triggered,
          - it allows to extend the methods in order to support adaptive stepsize.
    
    
        The predicted Nordsieck vector at step n+1 is computed from the Nordsieck vector at step n as follows:
    
          - Y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
          - S :sub:`1` (n+1) = h f(t :sub:`n+1` , Y :sub:`n+1` )
          - R :sub:`n+1` = (s :sub:`1` (n) - S :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
        where A is a rows shifting matrix (the lower left part is an identity matrix):
    
        .. code-block: java
        
                [ 0 0   ...  0 0 | 0 ]
                [ ---------------+---]
                [ 1 0   ...  0 0 | 0 ]
            A = [ 0 1   ...  0 0 | 0 ]
                [       ...      | 0 ]
                [ 0 0   ...  1 0 | 0 ]
                [ 0 0   ...  0 1 | 0 ]
         
        From this predicted vector, the corrected vector is computed as follows:
    
          - y :sub:`n+1` = y :sub:`n` + S :sub:`1` (n+1) + [ -1 +1 -1 +1 ... ±1 ] r :sub:`n+1`
          - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
          - r :sub:`n+1` = R :sub:`n+1` + (s :sub:`1` (n+1) - S :sub:`1` (n+1)) P :sup:`-1` u
    
        where the upper case Y :sub:`n+1` , S :sub:`1` (n+1) and R :sub:`n+1` represent the predicted states whereas the lower
        case y :sub:`n+1` , s :sub:`n+1` and r :sub:`n+1` represent the corrected states.
    
        The P :sup:`-1` u vector and the P :sup:`-1` A P matrix do not depend on the state, they only depend on k and therefore
        are precomputed once for all.
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_AdamsMoultonFieldIntegrator__T], int: int, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_AdamsMoultonFieldIntegrator__T], int: int, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...

class AdamsMoultonIntegrator(AdamsIntegrator):
    """
    public class AdamsMoultonIntegrator extends :class:`~org.hipparchus.ode.nonstiff.AdamsIntegrator`
    
        This class implements implicit Adams-Moulton integrators for Ordinary Differential Equations.
    
        Adams-Moulton methods (in fact due to Adams alone) are implicit multistep ODE solvers. This implementation is a
        variation of the classical one: it uses adaptive stepsize to implement error control, whereas classical implementations
        are fixed step size. The value of state vector at step n+1 is a simple combination of the value at step n and of the
        derivatives at steps n+1, n, n-1 ... Since y' :sub:`n+1` is needed to compute y :sub:`n+1` , another method must be used
        to compute a first estimate of y :sub:`n+1` , then compute y' :sub:`n+1` , then compute a final estimate of y :sub:`n+1`
        using the following formulas. Depending on the number k of previous steps one wants to use for computing the next value,
        different formulas are available for the final estimate:
    
          - k = 1: y :sub:`n+1` = y :sub:`n` + h y' :sub:`n+1`
          - k = 2: y :sub:`n+1` = y :sub:`n` + h (y' :sub:`n+1` +y' :sub:`n` )/2
          - k = 3: y :sub:`n+1` = y :sub:`n` + h (5y' :sub:`n+1` +8y' :sub:`n` -y' :sub:`n-1` )/12
          - k = 4: y :sub:`n+1` = y :sub:`n` + h (9y' :sub:`n+1` +19y' :sub:`n` -5y' :sub:`n-1` +y' :sub:`n-2` )/24
          - ...
    
    
        A k-steps Adams-Moulton method is of order k+1.
    
        There must be sufficient time for the :meth:`~org.hipparchus.ode.MultistepIntegrator.setStarterIntegrator` to take
        several steps between the the last reset event, and the end of integration, otherwise an exception may be thrown during
        integration. The user can adjust the end date of integration, or the step size of the starter integrator to ensure a
        sufficient number of steps can be completed before the end of integration.
    
        Implementation details
    ----------------------
    
    
        We define scaled derivatives s :sub:`i` (n) at step n as:
    
        .. code-block: java
        
         s :sub:`1` (n) = h y' :sub:`n`  for first derivative
         s :sub:`2` (n) = h :sup:`2` /2 y'' :sub:`n`  for second derivative
         s :sub:`3` (n) = h :sup:`3` /6 y''' :sub:`n`  for third derivative
         ...
         s :sub:`k` (n) = h :sup:`k` /k! y :sup:`(k)`  :sub:`n`  for k :sup:`th`  derivative
         
    
        The definitions above use the classical representation with several previous first derivatives. Lets define
    
        .. code-block: java
        
           q :sub:`n`  = [ s :sub:`1` (n-1) s :sub:`1` (n-2) ... s :sub:`1` (n-(k-1)) ] :sup:`T` 
         
        (we omit the k index in the notation for clarity). With these definitions, Adams-Moulton methods can be written:
    
          - k = 1: y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n+1)
          - k = 2: y :sub:`n+1` = y :sub:`n` + 1/2 s :sub:`1` (n+1) + [ 1/2 ] q :sub:`n+1`
          - k = 3: y :sub:`n+1` = y :sub:`n` + 5/12 s :sub:`1` (n+1) + [ 8/12 -1/12 ] q :sub:`n+1`
          - k = 4: y :sub:`n+1` = y :sub:`n` + 9/24 s :sub:`1` (n+1) + [ 19/24 -5/24 1/24 ] q :sub:`n+1`
          - ...
    
    
        Instead of using the classical representation with first derivatives only (y :sub:`n` , s :sub:`1` (n+1) and q
        :sub:`n+1` ), our implementation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same
        step (y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as:
    
        .. code-block: java
        
         r :sub:`n`  = [ s :sub:`2` (n), s :sub:`3` (n) ... s :sub:`k` (n) ] :sup:`T` 
         
        (here again we omit the k index in the notation for clarity)
    
        Taylor series formulas show that for any index offset i, s :sub:`1` (n-i) can be computed from s :sub:`1` (n), s
        :sub:`2` (n) ... s :sub:`k` (n), the formula being exact for degree k polynomials.
    
        .. code-block: java
        
         s :sub:`1` (n-i) = s :sub:`1` (n) + ∑ :sub:`j>0`  (j+1) (-i) :sup:`j`  s :sub:`j+1` (n)
         
        The previous formula can be used with several values for i to compute the transform between classical representation and
        Nordsieck vector. The transform between r :sub:`n` and q :sub:`n` resulting from the Taylor series formulas above is:
    
        .. code-block: java
        
         q :sub:`n`  = s :sub:`1` (n) u + P r :sub:`n` 
         
        where u is the [ 1 1 ... 1 ] :sup:`T` vector and P is the (k-1)Ã—(k-1) matrix built with the (j+1) (-i) :sup:`j` terms
        with i being the row number starting from 1 and j being the column number starting from 1:
    
        .. code-block: java
        
                [  -2   3   -4    5  ... ]
                [  -4  12  -32   80  ... ]
           P =  [  -6  27 -108  405  ... ]
                [  -8  48 -256 1280  ... ]
                [          ...           ]
         
    
        Using the Nordsieck vector has several advantages:
    
          - it greatly simplifies step interpolation as the interpolator mainly applies Taylor series formulas,
          - it simplifies step changes that occur when discrete events that truncate the step are triggered,
          - it allows to extend the methods in order to support adaptive stepsize.
    
    
        The predicted Nordsieck vector at step n+1 is computed from the Nordsieck vector at step n as follows:
    
          - Y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
          - S :sub:`1` (n+1) = h f(t :sub:`n+1` , Y :sub:`n+1` )
          - R :sub:`n+1` = (s :sub:`1` (n) - S :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
        where A is a rows shifting matrix (the lower left part is an identity matrix):
    
        .. code-block: java
        
                [ 0 0   ...  0 0 | 0 ]
                [ ---------------+---]
                [ 1 0   ...  0 0 | 0 ]
            A = [ 0 1   ...  0 0 | 0 ]
                [       ...      | 0 ]
                [ 0 0   ...  1 0 | 0 ]
                [ 0 0   ...  0 1 | 0 ]
         
        From this predicted vector, the corrected vector is computed as follows:
    
          - y :sub:`n+1` = y :sub:`n` + S :sub:`1` (n+1) + [ -1 +1 -1 +1 ... ±1 ] r :sub:`n+1`
          - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
          - r :sub:`n+1` = R :sub:`n+1` + (s :sub:`1` (n+1) - S :sub:`1` (n+1)) P :sup:`-1` u
    
        where the upper case Y :sub:`n+1` , S :sub:`1` (n+1) and R :sub:`n+1` represent the predicted states whereas the lower
        case y :sub:`n+1` , s :sub:`n+1` and r :sub:`n+1` represent the corrected states.
    
        The P :sup:`-1` u vector and the P :sup:`-1` A P matrix do not depend on the state, they only depend on k and therefore
        are precomputed once for all.
    """
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...

_EmbeddedRungeKuttaFieldIntegrator__T = typing.TypeVar('_EmbeddedRungeKuttaFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class EmbeddedRungeKuttaFieldIntegrator(AdaptiveStepsizeFieldIntegrator[_EmbeddedRungeKuttaFieldIntegrator__T], FieldButcherArrayProvider[_EmbeddedRungeKuttaFieldIntegrator__T], typing.Generic[_EmbeddedRungeKuttaFieldIntegrator__T]):
    """
    public abstract class EmbeddedRungeKuttaFieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator`<T> implements :class:`~org.hipparchus.ode.nonstiff.FieldButcherArrayProvider`<T>
    
        This class implements the common part of all embedded Runge-Kutta integrators for Ordinary Differential Equations.
    
        These methods are embedded explicit Runge-Kutta methods with two sets of coefficients allowing to estimate the error,
        their Butcher arrays are as follows :
    
        .. code-block: java
        
            0  |
           c2  | a21
           c3  | a31  a32
           ... |        ...
           cs  | as1  as2  ...  ass-1
               |--------------------------
               |  b1   b2  ...   bs-1  bs
               |  b'1  b'2 ...   b's-1 b's
         
    
        In fact, we rather use the array defined by ej = bj - b'j to compute directly the error rather than computing two
        estimates and then comparing them.
    
        Some methods are qualified as *fsal* (first same as last) methods. This means the last evaluation of the derivatives in
        one step is the same as the first in the next step. Then, this evaluation can be reused from one step to the next one
        and the cost of such a method is really s-1 evaluations despite the method still has s stages. This behaviour is true
        only for successful steps, if the step is rejected after the error estimation phase, no evaluation is saved. For an
        *fsal* method, we have cs = 1 and asi = bi for all i.
    """
    def getMaxGrowth(self) -> _EmbeddedRungeKuttaFieldIntegrator__T:
        """
            Get the maximal growth factor for stepsize control.
        
            Returns:
                maximal growth factor
        
        
        """
        ...
    def getMinReduction(self) -> _EmbeddedRungeKuttaFieldIntegrator__T:
        """
            Get the minimal reduction factor for stepsize control.
        
            Returns:
                minimal reduction factor
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Get the order of the method.
        
            Returns:
                order of the method
        
        
        """
        ...
    def getSafety(self) -> _EmbeddedRungeKuttaFieldIntegrator__T:
        """
            Get the safety factor for stepsize control.
        
            Returns:
                safety factor
        
        
        """
        ...
    def integrate(self, fieldExpandableODE: org.hipparchus.ode.FieldExpandableODE[_EmbeddedRungeKuttaFieldIntegrator__T], fieldODEState: org.hipparchus.ode.FieldODEState[_EmbeddedRungeKuttaFieldIntegrator__T], t: _EmbeddedRungeKuttaFieldIntegrator__T) -> org.hipparchus.ode.FieldODEStateAndDerivative[_EmbeddedRungeKuttaFieldIntegrator__T]: ...
    def setMaxGrowth(self, t: _EmbeddedRungeKuttaFieldIntegrator__T) -> None:
        """
            Set the maximal growth factor for stepsize control.
        
            Parameters:
                maxGrowth (:class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator`): maximal growth factor
        
        
        """
        ...
    def setMinReduction(self, t: _EmbeddedRungeKuttaFieldIntegrator__T) -> None:
        """
            Set the minimal reduction factor for stepsize control.
        
            Parameters:
                minReduction (:class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator`): minimal reduction factor
        
        
        """
        ...
    def setSafety(self, t: _EmbeddedRungeKuttaFieldIntegrator__T) -> None:
        """
            Set the safety factor for stepsize control.
        
            Parameters:
                safety (:class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator`): safety factor
        
        
        """
        ...

class EmbeddedRungeKuttaIntegrator(AdaptiveStepsizeIntegrator, ButcherArrayProvider):
    """
    public abstract class EmbeddedRungeKuttaIntegrator extends :class:`~org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator` implements :class:`~org.hipparchus.ode.nonstiff.ButcherArrayProvider`
    
        This class implements the common part of all embedded Runge-Kutta integrators for Ordinary Differential Equations.
    
        These methods are embedded explicit Runge-Kutta methods with two sets of coefficients allowing to estimate the error,
        their Butcher arrays are as follows :
    
        .. code-block: java
        
            0  |
           c2  | a21
           c3  | a31  a32
           ... |        ...
           cs  | as1  as2  ...  ass-1
               |--------------------------
               |  b1   b2  ...   bs-1  bs
               |  b'1  b'2 ...   b's-1 b's
         
    
        In fact, we rather use the array defined by ej = bj - b'j to compute directly the error rather than computing two
        estimates and then comparing them.
    
        Some methods are qualified as *fsal* (first same as last) methods. This means the last evaluation of the derivatives in
        one step is the same as the first in the next step. Then, this evaluation can be reused from one step to the next one
        and the cost of such a method is really s-1 evaluations despite the method still has s stages. This behaviour is true
        only for successful steps, if the step is rejected after the error estimation phase, no evaluation is saved. For an
        *fsal* method, we have cs = 1 and asi = bi for all i.
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
    def getOrder(self) -> int:
        """
            Get the order of the method.
        
            Returns:
                order of the method
        
        
        """
        ...
    def getSafety(self) -> float:
        """
            Get the safety factor for stepsize control.
        
            Returns:
                safety factor
        
        
        """
        ...
    @typing.overload
    def integrate(self, ordinaryDifferentialEquation: org.hipparchus.ode.OrdinaryDifferentialEquation, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...
    @typing.overload
    def integrate(self, expandableODE: org.hipparchus.ode.ExpandableODE, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...
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

class GraggBulirschStoerIntegrator(AdaptiveStepsizeIntegrator):
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    @typing.overload
    def integrate(self, ordinaryDifferentialEquation: org.hipparchus.ode.OrdinaryDifferentialEquation, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...
    @typing.overload
    def integrate(self, expandableODE: org.hipparchus.ode.ExpandableODE, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...
    def setControlFactors(self, double: float, double2: float, double3: float, double4: float) -> None: ...
    def setInterpolationControl(self, boolean: bool, int: int) -> None: ...
    def setOrderControl(self, int: int, double: float, double2: float) -> None: ...
    def setStabilityCheck(self, boolean: bool, int: int, int2: int, double: float) -> None: ...

_RungeKuttaFieldIntegrator__T = typing.TypeVar('_RungeKuttaFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class RungeKuttaFieldIntegrator(org.hipparchus.ode.AbstractFieldIntegrator[_RungeKuttaFieldIntegrator__T], FieldButcherArrayProvider[_RungeKuttaFieldIntegrator__T], typing.Generic[_RungeKuttaFieldIntegrator__T]):
    """
    public abstract class RungeKuttaFieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.AbstractFieldIntegrator`<T> implements :class:`~org.hipparchus.ode.nonstiff.FieldButcherArrayProvider`<T>
    
        This class implements the common part of all fixed step Runge-Kutta integrators for Ordinary Differential Equations.
    
        These methods are explicit Runge-Kutta methods, their Butcher arrays are as follows :
    
        .. code-block: java
        
            0  |
           c2  | a21
           c3  | a31  a32
           ... |        ...
           cs  | as1  as2  ...  ass-1
               |--------------------------
               |  b1   b2  ...   bs-1  bs
         
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.EulerFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.GillFieldIntegrator`, :class:`~org.hipparchus.ode.nonstiff.MidpointFieldIntegrator`
    """
    def integrate(self, fieldExpandableODE: org.hipparchus.ode.FieldExpandableODE[_RungeKuttaFieldIntegrator__T], fieldODEState: org.hipparchus.ode.FieldODEState[_RungeKuttaFieldIntegrator__T], t: _RungeKuttaFieldIntegrator__T) -> org.hipparchus.ode.FieldODEStateAndDerivative[_RungeKuttaFieldIntegrator__T]: ...
    def singleStep(self, fieldOrdinaryDifferentialEquation: org.hipparchus.ode.FieldOrdinaryDifferentialEquation[_RungeKuttaFieldIntegrator__T], t: _RungeKuttaFieldIntegrator__T, tArray: typing.List[_RungeKuttaFieldIntegrator__T], t3: _RungeKuttaFieldIntegrator__T) -> typing.List[_RungeKuttaFieldIntegrator__T]: ...

class RungeKuttaIntegrator(org.hipparchus.ode.AbstractIntegrator, ButcherArrayProvider):
    """
    public abstract class RungeKuttaIntegrator extends :class:`~org.hipparchus.ode.AbstractIntegrator` implements :class:`~org.hipparchus.ode.nonstiff.ButcherArrayProvider`
    
        This class implements the common part of all fixed step Runge-Kutta integrators for Ordinary Differential Equations.
    
        These methods are explicit Runge-Kutta methods, their Butcher arrays are as follows :
    
        .. code-block: java
        
            0  |
           c2  | a21
           c3  | a31  a32
           ... |        ...
           cs  | as1  as2  ...  ass-1
               |--------------------------
               |  b1   b2  ...   bs-1  bs
         
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.EulerIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.GillIntegrator`, :class:`~org.hipparchus.ode.nonstiff.MidpointIntegrator`
    """
    @typing.overload
    def integrate(self, ordinaryDifferentialEquation: org.hipparchus.ode.OrdinaryDifferentialEquation, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...
    @typing.overload
    def integrate(self, expandableODE: org.hipparchus.ode.ExpandableODE, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...
    def singleStep(self, ordinaryDifferentialEquation: org.hipparchus.ode.OrdinaryDifferentialEquation, double: float, doubleArray: typing.List[float], double3: float) -> typing.List[float]:
        """
            Fast computation of a single step of ODE integration.
        
            This method is intended for the limited use case of very fast computation of only one step without using any of the rich
            features of general integrators that may take some time to set up (i.e. no step handlers, no events handlers, no
            additional states, no interpolators, no error control, no evaluations count, no sanity checks ...). It handles the
            strict minimum of computation, so it can be embedded in outer loops.
        
            This method is *not* used at all by the :meth:`~org.hipparchus.ode.nonstiff.RungeKuttaIntegrator.integrate` method. It
            also completely ignores the step set at construction time, and uses only a single step to go from :code:`t0` to
            :code:`t`.
        
            As this method does not use any of the state-dependent features of the integrator, it should be reasonably thread-safe
            *if and only if* the provided differential equations are themselves thread-safe.
        
            Parameters:
                equations (:class:`~org.hipparchus.ode.OrdinaryDifferentialEquation`): differential equations to integrate
                t0 (double): initial time
                y0 (double[]): initial value of the state vector at t0
                t (double): target time for the integration (can be set to a value smaller than :code:`t0` for backward integration)
        
            Returns:
                state vector at :code:`t`
        
        
        """
        ...

_ClassicalRungeKuttaFieldIntegrator__T = typing.TypeVar('_ClassicalRungeKuttaFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class ClassicalRungeKuttaFieldIntegrator(RungeKuttaFieldIntegrator[_ClassicalRungeKuttaFieldIntegrator__T], typing.Generic[_ClassicalRungeKuttaFieldIntegrator__T]):
    """
    public class ClassicalRungeKuttaFieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.nonstiff.RungeKuttaFieldIntegrator`<T>
    
        This class implements the classical fourth order Runge-Kutta integrator for Ordinary Differential Equations (it is the
        most often used Runge-Kutta method).
    
        This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        .. code-block: java
        
            0  |  0    0    0    0
           1/2 | 1/2   0    0    0
           1/2 |  0   1/2   0    0
            1  |  0    0    1    0
               |--------------------
               | 1/6  1/3  1/3  1/6
         
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.EulerFieldIntegrator`, :class:`~org.hipparchus.ode.nonstiff.GillFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.MidpointFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ThreeEighthesFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.LutherFieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_ClassicalRungeKuttaFieldIntegrator__T], t: _ClassicalRungeKuttaFieldIntegrator__T): ...
    def getA(self) -> typing.List[typing.List[_ClassicalRungeKuttaFieldIntegrator__T]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[_ClassicalRungeKuttaFieldIntegrator__T]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[_ClassicalRungeKuttaFieldIntegrator__T]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...

class ClassicalRungeKuttaIntegrator(RungeKuttaIntegrator):
    """
    public class ClassicalRungeKuttaIntegrator extends :class:`~org.hipparchus.ode.nonstiff.RungeKuttaIntegrator`
    
        This class implements the classical fourth order Runge-Kutta integrator for Ordinary Differential Equations (it is the
        most often used Runge-Kutta method).
    
        This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        .. code-block: java
        
            0  |  0    0    0    0
           1/2 | 1/2   0    0    0
           1/2 |  0   1/2   0    0
            1  |  0    0    1    0
               |--------------------
               | 1/6  1/3  1/3  1/6
         
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.EulerIntegrator`, :class:`~org.hipparchus.ode.nonstiff.GillIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.MidpointIntegrator`, :class:`~org.hipparchus.ode.nonstiff.ThreeEighthesIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.LutherIntegrator`
    """
    def __init__(self, double: float): ...
    def getA(self) -> typing.List[typing.List[float]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[float]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[float]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...

_DormandPrince54FieldIntegrator__T = typing.TypeVar('_DormandPrince54FieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class DormandPrince54FieldIntegrator(EmbeddedRungeKuttaFieldIntegrator[_DormandPrince54FieldIntegrator__T], typing.Generic[_DormandPrince54FieldIntegrator__T]):
    """
    public class DormandPrince54FieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator`<T>
    
        This class implements the 5(4) Dormand-Prince integrator for Ordinary Differential Equations.
    
        This integrator is an embedded Runge-Kutta integrator of order 5(4) used in local extrapolation mode (i.e. the solution
        is computed using the high order formula) with stepsize control (and automatic step initialization) and continuous
        output. This method uses 7 functions evaluations per step. However, since this is an *fsal*, the last evaluation of one
        step is the same as the first evaluation of the next step and hence can be avoided. So the cost is really 6 functions
        evaluations per step.
    
        This method has been published (whithout the continuous output that was added by Shampine in 1986) in the following
        article :
    
        .. code-block: java
        
          A family of embedded Runge-Kutta formulae
          J. R. Dormand and P. J. Prince
          Journal of Computational and Applied Mathematics
          volume 6, no 1, 1980, pp. 19-26
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_DormandPrince54FieldIntegrator__T], double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_DormandPrince54FieldIntegrator__T], double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def getA(self) -> typing.List[typing.List[_DormandPrince54FieldIntegrator__T]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[_DormandPrince54FieldIntegrator__T]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[_DormandPrince54FieldIntegrator__T]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Get the order of the method.
        
            Specified by:
                :meth:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator.getOrder`Â in
                classÂ :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator`
        
            Returns:
                order of the method
        
        
        """
        ...

class DormandPrince54Integrator(EmbeddedRungeKuttaIntegrator):
    """
    public class DormandPrince54Integrator extends :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaIntegrator`
    
        This class implements the 5(4) Dormand-Prince integrator for Ordinary Differential Equations.
    
        This integrator is an embedded Runge-Kutta integrator of order 5(4) used in local extrapolation mode (i.e. the solution
        is computed using the high order formula) with stepsize control (and automatic step initialization) and continuous
        output. This method uses 7 functions evaluations per step. However, since this is an *fsal*, the last evaluation of one
        step is the same as the first evaluation of the next step and hence can be avoided. So the cost is really 6 functions
        evaluations per step.
    
        This method has been published (whithout the continuous output that was added by Shampine in 1986) in the following
        article :
    
        .. code-block: java
        
          A family of embedded Runge-Kutta formulae
          J. R. Dormand and P. J. Prince
          Journal of Computational and Applied Mathematics
          volume 6, no 1, 1980, pp. 19-26
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def getA(self) -> typing.List[typing.List[float]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[float]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[float]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Get the order of the method.
        
            Specified by:
                :meth:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaIntegrator.getOrder`Â in
                classÂ :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaIntegrator`
        
            Returns:
                order of the method
        
        
        """
        ...

_DormandPrince853FieldIntegrator__T = typing.TypeVar('_DormandPrince853FieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class DormandPrince853FieldIntegrator(EmbeddedRungeKuttaFieldIntegrator[_DormandPrince853FieldIntegrator__T], typing.Generic[_DormandPrince853FieldIntegrator__T]):
    """
    public class DormandPrince853FieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator`<T>
    
        This class implements the 8(5,3) Dormand-Prince integrator for Ordinary Differential Equations.
    
        This integrator is an embedded Runge-Kutta integrator of order 8(5,3) used in local extrapolation mode (i.e. the
        solution is computed using the high order formula) with stepsize control (and automatic step initialization) and
        continuous output. This method uses 12 functions evaluations per step for integration and 4 evaluations for
        interpolation. However, since the first interpolation evaluation is the same as the first integration evaluation of the
        next step, we have included it in the integrator rather than in the interpolator and specified the method was an *fsal*.
        Hence, despite we have 13 stages here, the cost is really 12 evaluations per step even if no interpolation is done, and
        the overcost of interpolation is only 3 evaluations.
    
        This method is based on an 8(6) method by Dormand and Prince (i.e. order 8 for the integration and order 6 for error
        estimation) modified by Hairer and Wanner to use a 5th order error estimator with 3rd order correction. This
        modification was introduced because the original method failed in some cases (wrong steps can be accepted when step size
        is too large, for example in the Brusselator problem) and also had *severe difficulties when applied to problems with
        discontinuities*. This modification is explained in the second edition of the first volume (Nonstiff Problems) of the
        reference book by Hairer, Norsett and Wanner: *Solving Ordinary Differential Equations* (Springer-Verlag, ISBN
        3-540-56670-8).
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_DormandPrince853FieldIntegrator__T], double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_DormandPrince853FieldIntegrator__T], double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def getA(self) -> typing.List[typing.List[_DormandPrince853FieldIntegrator__T]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[_DormandPrince853FieldIntegrator__T]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[_DormandPrince853FieldIntegrator__T]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Get the order of the method.
        
            Specified by:
                :meth:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator.getOrder`Â in
                classÂ :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator`
        
            Returns:
                order of the method
        
        
        """
        ...

class DormandPrince853Integrator(EmbeddedRungeKuttaIntegrator):
    """
    public class DormandPrince853Integrator extends :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaIntegrator`
    
        This class implements the 8(5,3) Dormand-Prince integrator for Ordinary Differential Equations.
    
        This integrator is an embedded Runge-Kutta integrator of order 8(5,3) used in local extrapolation mode (i.e. the
        solution is computed using the high order formula) with stepsize control (and automatic step initialization) and
        continuous output. This method uses 12 functions evaluations per step for integration and 4 evaluations for
        interpolation. However, since the first interpolation evaluation is the same as the first integration evaluation of the
        next step, we have included it in the integrator rather than in the interpolator and specified the method was an *fsal*.
        Hence, despite we have 13 stages here, the cost is really 12 evaluations per step even if no interpolation is done, and
        the overcost of interpolation is only 3 evaluations.
    
        This method is based on an 8(6) method by Dormand and Prince (i.e. order 8 for the integration and order 6 for error
        estimation) modified by Hairer and Wanner to use a 5th order error estimator with 3rd order correction. This
        modification was introduced because the original method failed in some cases (wrong steps can be accepted when step size
        is too large, for example in the Brusselator problem) and also had *severe difficulties when applied to problems with
        discontinuities*. This modification is explained in the second edition of the first volume (Nonstiff Problems) of the
        reference book by Hairer, Norsett and Wanner: *Solving Ordinary Differential Equations* (Springer-Verlag, ISBN
        3-540-56670-8).
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def getA(self) -> typing.List[typing.List[float]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[float]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[float]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Get the order of the method.
        
            Specified by:
                :meth:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaIntegrator.getOrder`Â in
                classÂ :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaIntegrator`
        
            Returns:
                order of the method
        
        
        """
        ...

_EulerFieldIntegrator__T = typing.TypeVar('_EulerFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class EulerFieldIntegrator(RungeKuttaFieldIntegrator[_EulerFieldIntegrator__T], typing.Generic[_EulerFieldIntegrator__T]):
    """
    public class EulerFieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.nonstiff.RungeKuttaFieldIntegrator`<T>
    
        This class implements a simple Euler integrator for Ordinary Differential Equations.
    
        The Euler algorithm is the simplest one that can be used to integrate ordinary differential equations. It is a simple
        inversion of the forward difference expression : :code:`f'=(f(t+h)-f(t))/h` which leads to :code:`f(t+h)=f(t)+hf'`. The
        interpolation scheme used for dense output is the linear scheme already used for integration.
    
        This algorithm looks cheap because it needs only one function evaluation per step. However, as it uses linear estimates,
        it needs very small steps to achieve high accuracy, and small steps lead to numerical errors and instabilities.
    
        This algorithm is almost never used and has been included in this package only as a comparison reference for more useful
        integrators.
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.MidpointFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.GillFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ThreeEighthesFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.LutherFieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_EulerFieldIntegrator__T], t: _EulerFieldIntegrator__T): ...
    def getA(self) -> typing.List[typing.List[_EulerFieldIntegrator__T]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[_EulerFieldIntegrator__T]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[_EulerFieldIntegrator__T]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...

class EulerIntegrator(RungeKuttaIntegrator):
    """
    public class EulerIntegrator extends :class:`~org.hipparchus.ode.nonstiff.RungeKuttaIntegrator`
    
        This class implements a simple Euler integrator for Ordinary Differential Equations.
    
        The Euler algorithm is the simplest one that can be used to integrate ordinary differential equations. It is a simple
        inversion of the forward difference expression : :code:`f'=(f(t+h)-f(t))/h` which leads to :code:`f(t+h)=f(t)+hf'`. The
        interpolation scheme used for dense output is the linear scheme already used for integration.
    
        This algorithm looks cheap because it needs only one function evaluation per step. However, as it uses linear estimates,
        it needs very small steps to achieve high accuracy, and small steps lead to numerical errors and instabilities.
    
        This algorithm is almost never used and has been included in this package only as a comparison reference for more useful
        integrators.
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.MidpointIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.GillIntegrator`, :class:`~org.hipparchus.ode.nonstiff.ThreeEighthesIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.LutherIntegrator`
    """
    def __init__(self, double: float): ...
    def getA(self) -> typing.List[typing.List[float]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[float]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[float]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...

_GillFieldIntegrator__T = typing.TypeVar('_GillFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class GillFieldIntegrator(RungeKuttaFieldIntegrator[_GillFieldIntegrator__T], typing.Generic[_GillFieldIntegrator__T]):
    """
    public class GillFieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.nonstiff.RungeKuttaFieldIntegrator`<T>
    
        This class implements the Gill fourth order Runge-Kutta integrator for Ordinary Differential Equations .
    
        This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        .. code-block: java
        
            0  |    0        0       0      0
           1/2 |   1/2       0       0      0
           1/2 | (q-1)/2  (2-q)/2    0      0
            1  |    0       -q/2  (2+q)/2   0
               |-------------------------------
               |   1/6    (2-q)/6 (2+q)/6  1/6
         
        where q = sqrt(2)
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.EulerFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.MidpointFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ThreeEighthesFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.LutherFieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_GillFieldIntegrator__T], t: _GillFieldIntegrator__T): ...
    def getA(self) -> typing.List[typing.List[_GillFieldIntegrator__T]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[_GillFieldIntegrator__T]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[_GillFieldIntegrator__T]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...

class GillIntegrator(RungeKuttaIntegrator):
    """
    public class GillIntegrator extends :class:`~org.hipparchus.ode.nonstiff.RungeKuttaIntegrator`
    
        This class implements the Gill fourth order Runge-Kutta integrator for Ordinary Differential Equations .
    
        This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        .. code-block: java
        
            0  |    0        0       0      0
           1/2 |   1/2       0       0      0
           1/2 | (q-1)/2  (2-q)/2    0      0
            1  |    0       -q/2  (2+q)/2   0
               |-------------------------------
               |   1/6    (2-q)/6 (2+q)/6  1/6
         
        where q = sqrt(2)
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.EulerIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.MidpointIntegrator`, :class:`~org.hipparchus.ode.nonstiff.ThreeEighthesIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.LutherIntegrator`
    """
    def __init__(self, double: float): ...
    def getA(self) -> typing.List[typing.List[float]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[float]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[float]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...

_HighamHall54FieldIntegrator__T = typing.TypeVar('_HighamHall54FieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class HighamHall54FieldIntegrator(EmbeddedRungeKuttaFieldIntegrator[_HighamHall54FieldIntegrator__T], typing.Generic[_HighamHall54FieldIntegrator__T]):
    """
    public class HighamHall54FieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator`<T>
    
        This class implements the 5(4) Higham and Hall integrator for Ordinary Differential Equations.
    
        This integrator is an embedded Runge-Kutta integrator of order 5(4) used in local extrapolation mode (i.e. the solution
        is computed using the high order formula) with stepsize control (and automatic step initialization) and continuous
        output. This method uses 7 functions evaluations per step.
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_HighamHall54FieldIntegrator__T], double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_HighamHall54FieldIntegrator__T], double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def getA(self) -> typing.List[typing.List[_HighamHall54FieldIntegrator__T]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[_HighamHall54FieldIntegrator__T]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[_HighamHall54FieldIntegrator__T]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Get the order of the method.
        
            Specified by:
                :meth:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator.getOrder`Â in
                classÂ :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator`
        
            Returns:
                order of the method
        
        
        """
        ...

class HighamHall54Integrator(EmbeddedRungeKuttaIntegrator):
    """
    public class HighamHall54Integrator extends :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaIntegrator`
    
        This class implements the 5(4) Higham and Hall integrator for Ordinary Differential Equations.
    
        This integrator is an embedded Runge-Kutta integrator of order 5(4) used in local extrapolation mode (i.e. the solution
        is computed using the high order formula) with stepsize control (and automatic step initialization) and continuous
        output. This method uses 7 functions evaluations per step.
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def getA(self) -> typing.List[typing.List[float]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[float]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[float]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Get the order of the method.
        
            Specified by:
                :meth:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaIntegrator.getOrder`Â in
                classÂ :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaIntegrator`
        
            Returns:
                order of the method
        
        
        """
        ...

_LutherFieldIntegrator__T = typing.TypeVar('_LutherFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class LutherFieldIntegrator(RungeKuttaFieldIntegrator[_LutherFieldIntegrator__T], typing.Generic[_LutherFieldIntegrator__T]):
    """
    public class LutherFieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.nonstiff.RungeKuttaFieldIntegrator`<T>
    
        This class implements the Luther sixth order Runge-Kutta integrator for Ordinary Differential Equations.
    
        This method is described in H. A. Luther 1968 paper ` An explicit Sixth-Order Runge-Kutta Formula
        <http://www.ams.org/journals/mcom/1968-22-102/S0025-5718-68-99876-1/S0025-5718-68-99876-1.pdf>`.
    
        This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        .. code-block: java
        
                0   |               0                     0                     0                     0                     0                     0
                1   |               1                     0                     0                     0                     0                     0
               1/2  |              3/8                   1/8                    0                     0                     0                     0
               2/3  |              8/27                  2/27                  8/27                   0                     0                     0
           (7-q)/14 | (  -21 +   9q)/392    (  -56 +   8q)/392    (  336 -  48q)/392    (  -63 +   3q)/392                  0                     0
           (7+q)/14 | (-1155 - 255q)/1960   ( -280 -  40q)/1960   (    0 - 320q)/1960   (   63 + 363q)/1960   ( 2352 + 392q)/1960                 0
                1   | (  330 + 105q)/180    (  120 +   0q)/180    ( -200 + 280q)/180    (  126 - 189q)/180    ( -686 - 126q)/180     ( 490 -  70q)/180
                    |--------------------------------------------------------------------------------------------------------------------------------------------------
                    |              1/20                   0                   16/45                  0                   49/180                 49/180         1/20
         
        where q = √21
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.EulerFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.GillFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.MidpointFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ThreeEighthesFieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_LutherFieldIntegrator__T], t: _LutherFieldIntegrator__T): ...
    def getA(self) -> typing.List[typing.List[_LutherFieldIntegrator__T]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[_LutherFieldIntegrator__T]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[_LutherFieldIntegrator__T]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...

class LutherIntegrator(RungeKuttaIntegrator):
    """
    public class LutherIntegrator extends :class:`~org.hipparchus.ode.nonstiff.RungeKuttaIntegrator`
    
        This class implements the Luther sixth order Runge-Kutta integrator for Ordinary Differential Equations.
    
        This method is described in H. A. Luther 1968 paper ` An explicit Sixth-Order Runge-Kutta Formula
        <http://www.ams.org/journals/mcom/1968-22-102/S0025-5718-68-99876-1/S0025-5718-68-99876-1.pdf>`.
    
        This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        .. code-block: java
        
                0   |               0                     0                     0                     0                     0                     0
                1   |               1                     0                     0                     0                     0                     0
               1/2  |              3/8                   1/8                    0                     0                     0                     0
               2/3  |              8/27                  2/27                  8/27                   0                     0                     0
           (7-q)/14 | (  -21 +   9q)/392    (  -56 +   8q)/392    (  336 -  48q)/392    (  -63 +   3q)/392                  0                     0
           (7+q)/14 | (-1155 - 255q)/1960   ( -280 -  40q)/1960   (    0 - 320q)/1960   (   63 + 363q)/1960   ( 2352 + 392q)/1960                 0
                1   | (  330 + 105q)/180    (  120 +   0q)/180    ( -200 + 280q)/180    (  126 - 189q)/180    ( -686 - 126q)/180     ( 490 -  70q)/180
                    |--------------------------------------------------------------------------------------------------------------------------------------------------
                    |              1/20                   0                   16/45                  0                   49/180                 49/180         1/20
         
        where q = √21
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.EulerIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.GillIntegrator`, :class:`~org.hipparchus.ode.nonstiff.MidpointIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ThreeEighthesIntegrator`
    """
    def __init__(self, double: float): ...
    def getA(self) -> typing.List[typing.List[float]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[float]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[float]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...

_MidpointFieldIntegrator__T = typing.TypeVar('_MidpointFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class MidpointFieldIntegrator(RungeKuttaFieldIntegrator[_MidpointFieldIntegrator__T], typing.Generic[_MidpointFieldIntegrator__T]):
    """
    public class MidpointFieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.nonstiff.RungeKuttaFieldIntegrator`<T>
    
        This class implements a second order Runge-Kutta integrator for Ordinary Differential Equations.
    
        This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        .. code-block: java
        
            0  |  0    0
           1/2 | 1/2   0
               |----------
               |  0    1
         
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.EulerFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.GillFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ThreeEighthesFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.LutherFieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_MidpointFieldIntegrator__T], t: _MidpointFieldIntegrator__T): ...
    def getA(self) -> typing.List[typing.List[_MidpointFieldIntegrator__T]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[_MidpointFieldIntegrator__T]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[_MidpointFieldIntegrator__T]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...

class MidpointIntegrator(RungeKuttaIntegrator):
    """
    public class MidpointIntegrator extends :class:`~org.hipparchus.ode.nonstiff.RungeKuttaIntegrator`
    
        This class implements a second order Runge-Kutta integrator for Ordinary Differential Equations.
    
        This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        .. code-block: java
        
            0  |  0    0
           1/2 | 1/2   0
               |----------
               |  0    1
         
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.EulerIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.GillIntegrator`, :class:`~org.hipparchus.ode.nonstiff.ThreeEighthesIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.LutherIntegrator`
    """
    def __init__(self, double: float): ...
    def getA(self) -> typing.List[typing.List[float]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[float]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[float]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...

_ThreeEighthesFieldIntegrator__T = typing.TypeVar('_ThreeEighthesFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class ThreeEighthesFieldIntegrator(RungeKuttaFieldIntegrator[_ThreeEighthesFieldIntegrator__T], typing.Generic[_ThreeEighthesFieldIntegrator__T]):
    """
    public class ThreeEighthesFieldIntegrator<T extends CalculusFieldElement<T>> extends :class:`~org.hipparchus.ode.nonstiff.RungeKuttaFieldIntegrator`<T>
    
        This class implements the 3/8 fourth order Runge-Kutta integrator for Ordinary Differential Equations.
    
        This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        .. code-block: java
        
            0  |  0    0    0    0
           1/3 | 1/3   0    0    0
           2/3 |-1/3   1    0    0
            1  |  1   -1    1    0
               |--------------------
               | 1/8  3/8  3/8  1/8
         
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.EulerFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.GillFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.MidpointFieldIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.LutherFieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_ThreeEighthesFieldIntegrator__T], t: _ThreeEighthesFieldIntegrator__T): ...
    def getA(self) -> typing.List[typing.List[_ThreeEighthesFieldIntegrator__T]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[_ThreeEighthesFieldIntegrator__T]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[_ThreeEighthesFieldIntegrator__T]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...

class ThreeEighthesIntegrator(RungeKuttaIntegrator):
    """
    public class ThreeEighthesIntegrator extends :class:`~org.hipparchus.ode.nonstiff.RungeKuttaIntegrator`
    
        This class implements the 3/8 fourth order Runge-Kutta integrator for Ordinary Differential Equations.
    
        This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        .. code-block: java
        
            0  |  0    0    0    0
           1/3 | 1/3   0    0    0
           2/3 |-1/3   1    0    0
            1  |  1   -1    1    0
               |--------------------
               | 1/8  3/8  3/8  1/8
         
    
        Also see:
            :class:`~org.hipparchus.ode.nonstiff.EulerIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.GillIntegrator`, :class:`~org.hipparchus.ode.nonstiff.MidpointIntegrator`,
            :class:`~org.hipparchus.ode.nonstiff.LutherIntegrator`
    """
    def __init__(self, double: float): ...
    def getA(self) -> typing.List[typing.List[float]]:
        """
            Get the internal weights from Butcher array (without the first empty row).
        
            Returns:
                internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.List[float]:
        """
            Get the external weights for the high order method from Butcher array.
        
            Returns:
                external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.List[float]:
        """
            Get the time steps from Butcher array (without the first zero).
        
            Returns:
                time steps from Butcher array (without the first zero
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.ode.nonstiff")``.

    AdamsBashforthFieldIntegrator: typing.Type[AdamsBashforthFieldIntegrator]
    AdamsBashforthIntegrator: typing.Type[AdamsBashforthIntegrator]
    AdamsFieldIntegrator: typing.Type[AdamsFieldIntegrator]
    AdamsIntegrator: typing.Type[AdamsIntegrator]
    AdamsMoultonFieldIntegrator: typing.Type[AdamsMoultonFieldIntegrator]
    AdamsMoultonIntegrator: typing.Type[AdamsMoultonIntegrator]
    AdamsNordsieckFieldTransformer: typing.Type[AdamsNordsieckFieldTransformer]
    AdamsNordsieckTransformer: typing.Type[AdamsNordsieckTransformer]
    AdaptiveStepsizeFieldIntegrator: typing.Type[AdaptiveStepsizeFieldIntegrator]
    AdaptiveStepsizeIntegrator: typing.Type[AdaptiveStepsizeIntegrator]
    ButcherArrayProvider: typing.Type[ButcherArrayProvider]
    ClassicalRungeKuttaFieldIntegrator: typing.Type[ClassicalRungeKuttaFieldIntegrator]
    ClassicalRungeKuttaIntegrator: typing.Type[ClassicalRungeKuttaIntegrator]
    DormandPrince54FieldIntegrator: typing.Type[DormandPrince54FieldIntegrator]
    DormandPrince54Integrator: typing.Type[DormandPrince54Integrator]
    DormandPrince853FieldIntegrator: typing.Type[DormandPrince853FieldIntegrator]
    DormandPrince853Integrator: typing.Type[DormandPrince853Integrator]
    EmbeddedRungeKuttaFieldIntegrator: typing.Type[EmbeddedRungeKuttaFieldIntegrator]
    EmbeddedRungeKuttaIntegrator: typing.Type[EmbeddedRungeKuttaIntegrator]
    EulerFieldIntegrator: typing.Type[EulerFieldIntegrator]
    EulerIntegrator: typing.Type[EulerIntegrator]
    FieldButcherArrayProvider: typing.Type[FieldButcherArrayProvider]
    GillFieldIntegrator: typing.Type[GillFieldIntegrator]
    GillIntegrator: typing.Type[GillIntegrator]
    GraggBulirschStoerIntegrator: typing.Type[GraggBulirschStoerIntegrator]
    HighamHall54FieldIntegrator: typing.Type[HighamHall54FieldIntegrator]
    HighamHall54Integrator: typing.Type[HighamHall54Integrator]
    LutherFieldIntegrator: typing.Type[LutherFieldIntegrator]
    LutherIntegrator: typing.Type[LutherIntegrator]
    MidpointFieldIntegrator: typing.Type[MidpointFieldIntegrator]
    MidpointIntegrator: typing.Type[MidpointIntegrator]
    RungeKuttaFieldIntegrator: typing.Type[RungeKuttaFieldIntegrator]
    RungeKuttaIntegrator: typing.Type[RungeKuttaIntegrator]
    StepsizeHelper: typing.Type[StepsizeHelper]
    ThreeEighthesFieldIntegrator: typing.Type[ThreeEighthesFieldIntegrator]
    ThreeEighthesIntegrator: typing.Type[ThreeEighthesIntegrator]
