
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.hipparchus
import org.hipparchus.linear
import org.hipparchus.ode
import org.hipparchus.ode.nonstiff.interpolators
import typing



_AdamsFieldIntegrator__T = typing.TypeVar('_AdamsFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdamsFieldIntegrator(org.hipparchus.ode.MultistepFieldIntegrator[_AdamsFieldIntegrator__T], typing.Generic[_AdamsFieldIntegrator__T]):
    """
    Base class for AdamsBashforthFieldIntegrator and AdamsMoultonFieldIntegrator integrators.
    """
    def integrate(self, equations: org.hipparchus.ode.FieldExpandableODE[_AdamsFieldIntegrator__T], initialState: org.hipparchus.ode.FieldODEState[_AdamsFieldIntegrator__T], finalTime: _AdamsFieldIntegrator__T) -> org.hipparchus.ode.FieldODEStateAndDerivative[_AdamsFieldIntegrator__T]:
        """
        Integrate the differential equations up to the given time.
        
        This method solves an Initial Value Problem (IVP).
        
        Since this method stores some internal state variables made available in its public interface during integration (getCurrentSignedStepsize), it is not thread-safe.
        
        Parameters:
            equations (FieldExpandableODE<AdamsFieldIntegrator> equations): differential equations to integrate
            initialState (FieldODEState<AdamsFieldIntegrator> initialState): initial state (time, primary and secondary state vectors)
            finalTime (AdamsFieldIntegrator): target time for the integration (can be set to a value smaller than t0 for backward integration)
        
        Returns:
            final state, its time will be the same as finalTime if integration reached its target, but may be different if
            some FieldODEEventHandler stops it at some point.
        
        Raises:
            hipparchus: if integration step is too small
            hipparchus: if the location of an event cannot be bracketed
            hipparchus: if the number of functions evaluations is exceeded
        
        
        """
        ...
    def updateHighOrderDerivativesPhase1(self, highOrder: org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsFieldIntegrator__T]) -> org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsFieldIntegrator__T]:
        """
        Update the high order scaled derivatives for Adams integrators (phase 1).
        
        The complete update of high order derivatives has a form similar to: \[ r_{n+1} = (s_1(n) - s_1(n+1)) P^{-1} u + P^{-1} A P r_n \] this method computes the P :sup:`-1` A P r :sub:`n` part.
        
        Parameters:
            highOrder (hipparchus<AdamsFieldIntegrator> highOrder): high order scaled derivatives (h :sup:`2` /2 y''... h :sup:`k` /k! y(k))
        
        Returns:
            updated high order derivatives
        
              - updateHighOrderDerivativesPhase2
        
        
        
        """
        ...
    def updateHighOrderDerivativesPhase2(self, start: typing.Union[typing.List[_AdamsFieldIntegrator__T], jpype.JArray], end: typing.Union[typing.List[_AdamsFieldIntegrator__T], jpype.JArray], highOrder: org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsFieldIntegrator__T]) -> None:
        """
        Update the high order scaled derivatives Adams integrators (phase 2).
        
        The complete update of high order derivatives has a form similar to: \[ r_{n+1} = (s_1(n) - s_1(n+1)) P^{-1} u + P^{-1} A P r_n \] this method computes the (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u part.
        
        Phase 1 of the update must already have been performed.
        
        Parameters:
            start (AdamsFieldIntegrator[]): first order scaled derivatives at step start
            end (AdamsFieldIntegrator[]): first order scaled derivatives at step end
            highOrder (hipparchus<AdamsFieldIntegrator> highOrder): high order scaled derivatives, will be modified (h :sup:`2` /2 y''... h :sup:`k` /k! y(k))
        
              - updateHighOrderDerivativesPhase1
        
        
        
        """
        ...

class AdamsIntegrator(org.hipparchus.ode.MultistepIntegrator):
    """
    Base class for AdamsBashforthIntegrator and AdamsMoultonIntegrator integrators.
    """
    @typing.overload
    def integrate(self, ordinaryDifferentialEquation: org.hipparchus.ode.OrdinaryDifferentialEquation, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...
    @typing.overload
    def integrate(self, expandableODE: org.hipparchus.ode.ExpandableODE, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...
    def updateHighOrderDerivativesPhase1(self, highOrder: org.hipparchus.linear.Array2DRowRealMatrix) -> org.hipparchus.linear.Array2DRowRealMatrix:
        """
        Update the high order scaled derivatives for Adams integrators (phase 1).
        
        The complete update of high order derivatives has a form similar to: \[ r_{n+1} = (s_1(n) - s_1(n+1)) P^{-1} u + P^{-1} A P r_n \] this method computes the P :sup:`-1` A P r :sub:`n` part.
        
        Parameters:
            highOrder (hipparchus): high order scaled derivatives (h :sup:`2` /2 y''... h :sup:`k` /k! y(k))
        
        Returns:
            updated high order derivatives
        
              - updateHighOrderDerivativesPhase2
        
        
        
        """
        ...
    def updateHighOrderDerivativesPhase2(self, start: typing.Union[typing.List[float], jpype.JArray], end: typing.Union[typing.List[float], jpype.JArray], highOrder: org.hipparchus.linear.Array2DRowRealMatrix) -> None:
        """
        Update the high order scaled derivatives Adams integrators (phase 2).
        
        The complete update of high order derivatives has a form similar to: \[ r_{n+1} = (s_1(n) - s_1(n+1)) P^{-1} u + P^{-1} A P r_n \] this method computes the (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u part.
        
        Phase 1 of the update must already have been performed.
        
        Parameters:
            start (double[]): first order scaled derivatives at step start
            end (double[]): first order scaled derivatives at step end
            highOrder (hipparchus): high order scaled derivatives, will be modified (h :sup:`2` /2 y''... h :sup:`k` /k! y(k))
        
              - updateHighOrderDerivativesPhase1
        
        
        
        """
        ...

_AdamsNordsieckFieldTransformer__T = typing.TypeVar('_AdamsNordsieckFieldTransformer__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdamsNordsieckFieldTransformer(typing.Generic[_AdamsNordsieckFieldTransformer__T]):
    """
    Transformer to Nordsieck vectors for Adams integrators.
    
    This class is used by AdamsBashforthIntegrator and AdamsMoultonIntegrator integrators to convert between classical representation with several previous first derivatives and Nordsieck representation with higher order scaled derivatives.
    
    We define scaled derivatives s :sub:`i` (n) at step n as: \[ \left\{\begin{align} s_1(n) &= h y'_n \text{ for first derivative}\\ s_2(n) &= \frac{h^2}{2} y_n'' \text{ for second derivative}\\ s_3(n) &= \frac{h^3}{6} y_n''' \text{ for third derivative}\\ &\cdots\\ s_k(n) &= \frac{h^k}{k!} y_n^{(k)} \text{ for } k^\mathrm{th} \text{ derivative} \end{align}\right. \]
    
    With the previous definition, the classical representation of multistep methods uses first derivatives only, i.e. it handles y :sub:`n` , s :sub:`1` (n) and q :sub:`n` where q :sub:`n` is defined as: \[ q_n = [ s_1(n-1) s_1(n-2) \ldots s_1(n-(k-1)) ]^T \] (we omit the k index in the notation for clarity).
    
    Another possible representation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same step, i.e it handles y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as: \[ r_n = [ s_2(n), s_3(n) \ldots s_k(n) ]^T \] (here again we omit the k index in the notation for clarity)
    
    Taylor series formulas show that for any index offset i, s :sub:`1` (n-i) can be computed from s :sub:`1` (n), s :sub:`2` (n) ... s :sub:`k` (n), the formula being exact for degree k polynomials. \[ s_1(n-i) = s_1(n) + \sum_{j\gt 0} (j+1) (-i)^j s_{j+1}(n) \] The previous formula can be used with several values for i to compute the transform between classical representation and Nordsieck vector at step end. The transform between r :sub:`n` and q :sub:`n` resulting from the Taylor series formulas above is: \[ q_n = s_1(n) u + P r_n \] where u is the [ 1 1 ... 1 ] :sup:`T` vector and P is the (k-1)×(k-1) matrix built with the \((j+1) (-i)^j\) terms with i being the row number starting from 1 and j being the column number starting from 1: \[ P=\begin{bmatrix} -2 & 3 & -4 & 5 & \ldots \\ -4 & 12 & -32 & 80 & \ldots \\ -6 & 27 & -108 & 405 & \ldots \\ -8 & 48 & -256 & 1280 & \ldots \\ & & \ldots\\ \end{bmatrix} \]
    
    Changing -i into +i in the formula above can be used to compute a similar transform between classical representation and Nordsieck vector at step start. The resulting matrix is simply the absolute value of matrix P.
    
    For AdamsBashforthIntegrator method, the Nordsieck vector at step n+1 is computed from the Nordsieck vector at step n as follows:
    
      - y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
      - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
      - r :sub:`n+1` = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
    where A is a rows shifting matrix (the lower left part is an identity matrix):
    
            [ 0 0   ...  0 0 | 0 ] [ ---------------+---] [ 1 0   ...  0 0 | 0 ] A = [ 0 1   ...  0 0 | 0 ] [       ...      | 0 ] [ 0 0   ...  1 0 | 0 ] [ 0 0   ...  0 1 | 0 ]
    
    For AdamsMoultonIntegrator method, the predicted Nordsieck vector at step n+1 is computed from the Nordsieck vector at step n as follows:
    
      - Y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
      - S :sub:`1` (n+1) = h f(t :sub:`n+1` , Y :sub:`n+1` )
      - R :sub:`n+1` = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
    From this predicted vector, the corrected vector is computed as follows:
    
      - y :sub:`n+1` = y :sub:`n` + S :sub:`1` (n+1) + [ -1 +1 -1 +1 ... ±1 ] r :sub:`n+1`
      - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
      - r :sub:`n+1` = R :sub:`n+1` + (s :sub:`1` (n+1) - S :sub:`1` (n+1)) P :sup:`-1` u
    
    where the upper case Y :sub:`n+1` , S :sub:`1` (n+1) and R :sub:`n+1` represent the predicted states whereas the lower case y :sub:`n+1` , s :sub:`n+1` and r :sub:`n+1` represent the corrected states.
    
    We observe that both methods use similar update formulas. In both cases a P :sup:`-1` u vector and a P :sup:`-1` A P matrix are used that do not depend on the state, they only depend on k. This class handles these transformations.
    """
    _getInstance__T = typing.TypeVar('_getInstance__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getInstance(field: org.hipparchus.Field[_getInstance__T], nSteps: int) -> 'AdamsNordsieckFieldTransformer'[_getInstance__T]:
        """
        Get the Nordsieck transformer for a given field and number of steps.
        
        Parameters:
            field (hipparchus<T> field): field to which the time and state vector elements belong
            nSteps (int): number of steps of the multistep method (excluding the one being computed)
        
        Returns:
            Nordsieck transformer for the specified field and number of steps
        
        
        """
        ...
    def initializeHighOrderDerivatives(self, h: _AdamsNordsieckFieldTransformer__T, t: typing.Union[typing.List[_AdamsNordsieckFieldTransformer__T], jpype.JArray], y: typing.Union[typing.List[typing.MutableSequence[_AdamsNordsieckFieldTransformer__T]], jpype.JArray], yDot: typing.Union[typing.List[typing.MutableSequence[_AdamsNordsieckFieldTransformer__T]], jpype.JArray]) -> org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsNordsieckFieldTransformer__T]:
        """
        Initialize the high order scaled derivatives at step start.
        
        Parameters:
            h (AdamsNordsieckFieldTransformer): step size to use for scaling
            t (AdamsNordsieckFieldTransformer[]): first steps times
            y (AdamsNordsieckFieldTransformer[][]): first steps states
            yDot (AdamsNordsieckFieldTransformer[][]): first steps derivatives
        
        Returns:
            Nordieck vector at start of first step (h :sup:`2` /2 y'' :sub:`n` , h :sup:`3` /6 y''' :sub:`n` ... h :sup:`k` /k! y
            :sup:`(k)` :sub:`n` )
        
        
        """
        ...
    def updateHighOrderDerivativesPhase1(self, highOrder: org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsNordsieckFieldTransformer__T]) -> org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsNordsieckFieldTransformer__T]:
        """
        Update the high order scaled derivatives for Adams integrators (phase 1).
        
        The complete update of high order derivatives has a form similar to: \[ r_{n+1} = (s_1(n) - s_1(n+1)) P^{-1} u + P^{-1} A P r_n \] this method computes the P :sup:`-1` A P r :sub:`n` part.
        
        Parameters:
            highOrder (hipparchus<AdamsNordsieckFieldTransformer> highOrder): high order scaled derivatives (h :sup:`2` /2 y''... h :sup:`k` /k! y(k))
        
        Returns:
            updated high order derivatives
        
              - updateHighOrderDerivativesPhase2
        
        
        
        """
        ...
    def updateHighOrderDerivativesPhase2(self, start: typing.Union[typing.List[_AdamsNordsieckFieldTransformer__T], jpype.JArray], end: typing.Union[typing.List[_AdamsNordsieckFieldTransformer__T], jpype.JArray], highOrder: org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsNordsieckFieldTransformer__T]) -> None:
        """
        Update the high order scaled derivatives Adams integrators (phase 2).
        
        The complete update of high order derivatives has a form similar to: \[ r_{n+1} = (s_1(n) - s_1(n+1)) P^{-1} u + P^{-1} A P r_n \] this method computes the (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u part.
        
        Phase 1 of the update must already have been performed.
        
        Parameters:
            start (AdamsNordsieckFieldTransformer[]): first order scaled derivatives at step start
            end (AdamsNordsieckFieldTransformer[]): first order scaled derivatives at step end
            highOrder (hipparchus<AdamsNordsieckFieldTransformer> highOrder): high order scaled derivatives, will be modified (h :sup:`2` /2 y''... h :sup:`k` /k! y(k))
        
              - updateHighOrderDerivativesPhase1
        
        
        
        """
        ...

class AdamsNordsieckTransformer:
    """
    Transformer to Nordsieck vectors for Adams integrators.
    
    This class is used by AdamsBashforthIntegrator and AdamsMoultonIntegrator integrators to convert between classical representation with several previous first derivatives and Nordsieck representation with higher order scaled derivatives.
    
    We define scaled derivatives s :sub:`i` (n) at step n as: \[ \left\{\begin{align} s_1(n) &= h y'_n \text{ for first derivative}\\ s_2(n) &= \frac{h^2}{2} y_n'' \text{ for second derivative}\\ s_3(n) &= \frac{h^3}{6} y_n''' \text{ for third derivative}\\ &\cdots\\ s_k(n) &= \frac{h^k}{k!} y_n^{(k)} \text{ for } k^\mathrm{th} \text{ derivative} \end{align}\right. \]
    
    With the previous definition, the classical representation of multistep methods uses first derivatives only, i.e. it handles y :sub:`n` , s :sub:`1` (n) and q :sub:`n` where q :sub:`n` is defined as: \[ q_n = [ s_1(n-1) s_1(n-2) \ldots s_1(n-(k-1)) ]^T \] (we omit the k index in the notation for clarity).
    
    Another possible representation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same step, i.e it handles y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as: \[ r_n = [ s_2(n), s_3(n) \ldots s_k(n) ]^T \] (here again we omit the k index in the notation for clarity)
    
    Taylor series formulas show that for any index offset i, s :sub:`1` (n-i) can be computed from s :sub:`1` (n), s :sub:`2` (n) ... s :sub:`k` (n), the formula being exact for degree k polynomials. \[ s_1(n-i) = s_1(n) + \sum_{j\gt 0} (j+1) (-i)^j s_{j+1}(n) \] The previous formula can be used with several values for i to compute the transform between classical representation and Nordsieck vector at step end. The transform between r :sub:`n` and q :sub:`n` resulting from the Taylor series formulas above is: \[ q_n = s_1(n) u + P r_n \] where u is the [ 1 1 ... 1 ] :sup:`T` vector and P is the (k-1)×(k-1) matrix built with the \((j+1) (-i)^j\) terms with i being the row number starting from 1 and j being the column number starting from 1: \[ P=\begin{bmatrix} -2 & 3 & -4 & 5 & \ldots \\ -4 & 12 & -32 & 80 & \ldots \\ -6 & 27 & -108 & 405 & \ldots \\ -8 & 48 & -256 & 1280 & \ldots \\ & & \ldots\\ \end{bmatrix} \]
    
    Changing -i into +i in the formula above can be used to compute a similar transform between classical representation and Nordsieck vector at step start. The resulting matrix is simply the absolute value of matrix P.
    
    For AdamsBashforthIntegrator method, the Nordsieck vector at step n+1 is computed from the Nordsieck vector at step n as follows:
    
      - y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
      - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
      - r :sub:`n+1` = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
    where A is a rows shifting matrix (the lower left part is an identity matrix):
    
            [ 0 0   ...  0 0 | 0 ] [ ---------------+---] [ 1 0   ...  0 0 | 0 ] A = [ 0 1   ...  0 0 | 0 ] [       ...      | 0 ] [ 0 0   ...  1 0 | 0 ] [ 0 0   ...  0 1 | 0 ]
    
    For AdamsMoultonIntegrator method, the predicted Nordsieck vector at step n+1 is computed from the Nordsieck vector at step n as follows:
    
      - Y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
      - S :sub:`1` (n+1) = h f(t :sub:`n+1` , Y :sub:`n+1` )
      - R :sub:`n+1` = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
    From this predicted vector, the corrected vector is computed as follows:
    
      - y :sub:`n+1` = y :sub:`n` + S :sub:`1` (n+1) + [ -1 +1 -1 +1 ... ±1 ] r :sub:`n+1`
      - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
      - r :sub:`n+1` = R :sub:`n+1` + (s :sub:`1` (n+1) - S :sub:`1` (n+1)) P :sup:`-1` u
    
    where the upper case Y :sub:`n+1` , S :sub:`1` (n+1) and R :sub:`n+1` represent the predicted states whereas the lower case y :sub:`n+1` , s :sub:`n+1` and r :sub:`n+1` represent the corrected states.
    
    We observe that both methods use similar update formulas. In both cases a P :sup:`-1` u vector and a P :sup:`-1` A P matrix are used that do not depend on the state, they only depend on k. This class handles these transformations.
    """
    @staticmethod
    def getInstance(nSteps: int) -> 'AdamsNordsieckTransformer':
        """
        Get the Nordsieck transformer for a given number of steps.
        
        Parameters:
            nSteps (int): number of steps of the multistep method (excluding the one being computed)
        
        Returns:
            Nordsieck transformer for the specified number of steps
        
        
        """
        ...
    def initializeHighOrderDerivatives(self, h: float, t: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], yDot: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> org.hipparchus.linear.Array2DRowRealMatrix:
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
    def updateHighOrderDerivativesPhase1(self, highOrder: org.hipparchus.linear.Array2DRowRealMatrix) -> org.hipparchus.linear.Array2DRowRealMatrix:
        """
        Update the high order scaled derivatives for Adams integrators (phase 1).
        
        The complete update of high order derivatives has a form similar to: \[ r_{n+1} = (s_1(n) - s_1(n+1)) P^{-1} u + P^{-1} A P r_n \] this method computes the P :sup:`-1` A P r :sub:`n` part.
        
        Parameters:
            highOrder (hipparchus): high order scaled derivatives (h :sup:`2` /2 y''... h :sup:`k` /k! y(k))
        
        Returns:
            updated high order derivatives
        
              - updateHighOrderDerivativesPhase2
        
        
        
        """
        ...
    def updateHighOrderDerivativesPhase2(self, start: typing.Union[typing.List[float], jpype.JArray], end: typing.Union[typing.List[float], jpype.JArray], highOrder: org.hipparchus.linear.Array2DRowRealMatrix) -> None:
        """
        Update the high order scaled derivatives Adams integrators (phase 2).
        
        The complete update of high order derivatives has a form similar to: \[ r_{n+1} = (s_1(n) - s_1(n+1)) P^{-1} u + P^{-1} A P r_n \] this method computes the (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u part.
        
        Phase 1 of the update must already have been performed.
        
        Parameters:
            start (double[]): first order scaled derivatives at step start
            end (double[]): first order scaled derivatives at step end
            highOrder (hipparchus): high order scaled derivatives, will be modified (h :sup:`2` /2 y''... h :sup:`k` /k! y(k))
        
              - updateHighOrderDerivativesPhase1
        
        
        
        """
        ...

_AdaptiveStepsizeFieldIntegrator__T = typing.TypeVar('_AdaptiveStepsizeFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdaptiveStepsizeFieldIntegrator(org.hipparchus.ode.AbstractFieldIntegrator[_AdaptiveStepsizeFieldIntegrator__T], typing.Generic[_AdaptiveStepsizeFieldIntegrator__T]):
    """
    This abstract class holds the common part of all adaptive stepsize integrators for Ordinary Differential Equations.
    
    These algorithms perform integration with stepsize control, which means the user does not specify the integration step but rather a tolerance on error. The error threshold is computed as
    
     threshold_i = absTol_i + relTol_i * max (abs (ym), abs (ym+1))
    
    where absTol_i is the absolute tolerance for component i of the state vector and relTol_i is the relative tolerance for the same component. The user can also use only two scalar values absTol and relTol which will be used for all components.
    
    Note that only the getPrimaryState of the state vector is used for stepsize control. The getSecondaryState of the state vector are explicitly ignored for stepsize control.
    
    If the estimated error for ym+1 is such that
    
     sqrt((sum (errEst_i / threshold_i)^2 ) / n) < 1
    
    (where n is the main set dimension) then the step is accepted, otherwise the step is rejected and a new attempt is made with a new stepsize.
    """
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
    def initializeStep(self, forward: bool, order: int, scale: typing.Union[typing.List[_AdaptiveStepsizeFieldIntegrator__T], jpype.JArray], state0: org.hipparchus.ode.FieldODEStateAndDerivative[_AdaptiveStepsizeFieldIntegrator__T]) -> float:
        """
        Initialize the integration step.
        
        Parameters:
            forward (boolean): forward integration indicator
            order (int): order of the method
            scale (AdaptiveStepsizeFieldIntegrator[]): scaling vector for the state vector (can be shorter than state vector)
            state0 (FieldODEStateAndDerivative<AdaptiveStepsizeFieldIntegrator> state0): state at integration start time
        
        Returns:
            first integration step
        
        Raises:
            hipparchus: if the number of functions evaluations is exceeded
            hipparchus: if arrays dimensions do not match equations settings
        
        
        """
        ...
    def setInitialStepSize(self, initialStepSize: float) -> None:
        """
        Set the initial step size.
        
        This method allows the user to specify an initial positive step size instead of letting the integrator guess it by itself. If this method is not called before integration is started, the initial step size will be estimated by the integrator.
        
        Parameters:
            initialStepSize (double): initial step size to use (must be positive even for backward integration ; providing a negative value or a value outside
                of the min/max step interval will lead the integrator to ignore the value and compute the initial step size by itself)
        
        
        """
        ...
    @typing.overload
    def setStepSizeControl(self, double: float, double2: float, double3: float, double4: float) -> None:
        """
        Set the adaptive step size control parameters.
        
        A side effect of this method is to also reset the initial step so it will be automatically computed by the integrator if setInitialStepSize is not called by the user.
        
        Parameters:
            minimalStep (double): minimal step (must be positive even for backward integration), the last step can be smaller than this
            maximalStep (double): maximal step (must be positive even for backward integration)
            absoluteTolerance (double): allowed absolute error
            relativeTolerance (double): allowed relative error
        
        Set the adaptive step size control parameters.
        
        A side effect of this method is to also reset the initial step so it will be automatically computed by the integrator if setInitialStepSize is not called by the user.
        
        Parameters:
            minimalStep (double): minimal step (must be positive even for backward integration), the last step can be smaller than this
            maximalStep (double): maximal step (must be positive even for backward integration)
            absoluteTolerance (double[]): allowed absolute error
            relativeTolerance (double[]): allowed relative error
        
        
        """
        ...
    @typing.overload
    def setStepSizeControl(self, double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None: ...

class AdaptiveStepsizeIntegrator(org.hipparchus.ode.AbstractIntegrator):
    """
    This abstract class holds the common part of all adaptive stepsize integrators for Ordinary Differential Equations.
    
    These algorithms perform integration with stepsize control, which means the user does not specify the integration step but rather a tolerance on error. The error threshold is computed as
    
     threshold_i = absTol_i + relTol_i * max (abs (ym), abs (ym+1))
    
    where absTol_i is the absolute tolerance for component i of the state vector and relTol_i is the relative tolerance for the same component. The user can also use only two scalar values absTol and relTol which will be used for all components.
    
    If the Ordinary Differential Equations is an ExpandableODE rather than a OrdinaryDifferentialEquation, then only the getPrimary of the state vector is used for stepsize control, not the complete state vector.
    
    If the estimated error for ym+1 is such that
    
     sqrt((sum (errEst_i / threshold_i)^2 ) / n) < 1
    
    (where n is the main set dimension) then the step is accepted, otherwise the step is rejected and a new attempt is made with a new stepsize.
    """
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
    def initializeStep(self, forward: bool, order: int, scale: typing.Union[typing.List[float], jpype.JArray], state0: org.hipparchus.ode.ODEStateAndDerivative) -> float:
        """
        Initialize the integration step.
        
        Parameters:
            forward (boolean): forward integration indicator
            order (int): order of the method
            scale (double[]): scaling vector for the state vector (can be shorter than state vector)
            state0 (ODEStateAndDerivative): state at integration start time
        
        Returns:
            first integration step
        
        Raises:
            hipparchus: if the number of functions evaluations is exceeded
            hipparchus: if arrays dimensions do not match equations settings
        
        
        """
        ...
    def setInitialStepSize(self, initialStepSize: float) -> None:
        """
        Set the initial step size.
        
        This method allows the user to specify an initial positive step size instead of letting the integrator guess it by itself. If this method is not called before integration is started, the initial step size will be estimated by the integrator.
        
        Parameters:
            initialStepSize (double): initial step size to use (must be positive even for backward integration ; providing a negative value or a value outside
                of the min/max step interval will lead the integrator to ignore the value and compute the initial step size by itself)
        
        
        """
        ...
    @typing.overload
    def setStepSizeControl(self, double: float, double2: float, double3: float, double4: float) -> None:
        """
        Set the adaptive step size control parameters.
        
        A side effect of this method is to also reset the initial step so it will be automatically computed by the integrator if setInitialStepSize is not called by the user.
        
        Parameters:
            minimalStep (double): minimal step (must be positive even for backward integration), the last step can be smaller than this
            maximalStep (double): maximal step (must be positive even for backward integration)
            absoluteTolerance (double): allowed absolute error
            relativeTolerance (double): allowed relative error
        
        Set the adaptive step size control parameters.
        
        A side effect of this method is to also reset the initial step so it will be automatically computed by the integrator if setInitialStepSize is not called by the user.
        
        Parameters:
            minimalStep (double): minimal step (must be positive even for backward integration), the last step can be smaller than this
            maximalStep (double): maximal step (must be positive even for backward integration)
            absoluteTolerance (double[]): allowed absolute error
            relativeTolerance (double[]): allowed relative error
        
        
        """
        ...
    @typing.overload
    def setStepSizeControl(self, double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None: ...

class ButcherArrayProvider:
    """
    This interface represents an integrator based on Butcher arrays.
    
          - FixedStepRungeKuttaIntegrator
          - EmbeddedRungeKuttaIntegrator
    """
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[float]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[float]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...

_FieldButcherArrayProvider__T = typing.TypeVar('_FieldButcherArrayProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldButcherArrayProvider(typing.Generic[_FieldButcherArrayProvider__T]):
    """
    This interface represents an integrator based on Butcher arrays.
    
          - FixedStepRungeKuttaFieldIntegrator
          - EmbeddedRungeKuttaFieldIntegrator
    """
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[_FieldButcherArrayProvider__T]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[_FieldButcherArrayProvider__T]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[_FieldButcherArrayProvider__T]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...

class StepsizeHelper:
    """
    Helper for adaptive stepsize control.
    
    Since:
        2.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    _filterStep_1__T = typing.TypeVar('_filterStep_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def filterStep(self, double: float, boolean: bool, boolean2: bool) -> float: ...
    @typing.overload
    def filterStep(self, t: _filterStep_1__T, boolean: bool, boolean2: bool) -> _filterStep_1__T: ...
    def getDummyStepsize(self) -> float:
        """
        Get a dummy step size.
        
        Returns:
            geometric mean of getMinStep and
            getMaxStep
        
        
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
    def getRelativeTolerance(self, i: int) -> float:
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
    def getTolerance(self, i: int, scale: float) -> float:
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
    def getTolerance(self, i: int, scale: _getTolerance_1__T) -> _getTolerance_1__T:
        """
        Get the tolerance for one component.
        
        Parameters:
            i (int): component to select
            scale (T): scale factor for relative tolerance (i.e. y[i])
        
        Returns:
            tolerance for selected component
        
        
        """
        ...
    def setInitialStepSize(self, initialStepSize: float) -> None:
        """
        Set the initial step size.
        
        This method allows the user to specify an initial positive step size instead of letting the integrator guess it by itself. If this method is not called before integration is started, the initial step size will be estimated by the integrator.
        
        Parameters:
            initialStepSize (double): initial step size to use (must be positive even for backward integration ; providing a negative value or a value outside
                of the min/max step interval will lead the integrator to ignore the value and compute the initial step size by itself)
        
        
        """
        ...

_AdamsBashforthFieldIntegrator__T = typing.TypeVar('_AdamsBashforthFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdamsBashforthFieldIntegrator(AdamsFieldIntegrator[_AdamsBashforthFieldIntegrator__T], typing.Generic[_AdamsBashforthFieldIntegrator__T]):
    """
    This class implements explicit Adams-Bashforth integrators for Ordinary Differential Equations.
    
    Adams-Bashforth methods (in fact due to Adams alone) are explicit multistep ODE solvers. This implementation is a variation of the classical one: it uses adaptive stepsize to implement error control, whereas classical implementations are fixed step size. The value of state vector at step n+1 is a simple combination of the value at step n and of the derivatives at steps n, n-1, n-2 ... Depending on the number k of previous steps one wants to use for computing the next value, different formulas are available:
    
      - k = 1: y :sub:`n+1` = y :sub:`n` + h y' :sub:`n`
      - k = 2: y :sub:`n+1` = y :sub:`n` + h (3y' :sub:`n` -y' :sub:`n-1` )/2
      - k = 3: y :sub:`n+1` = y :sub:`n` + h (23y' :sub:`n` -16y' :sub:`n-1` +5y' :sub:`n-2` )/12
      - k = 4: y :sub:`n+1` = y :sub:`n` + h (55y' :sub:`n` -59y' :sub:`n-1` +37y' :sub:`n-2` -9y' :sub:`n-3` )/24
      - ...
    
    A k-steps Adams-Bashforth method is of order k.
    
    There must be sufficient time for the setStarterIntegrator to take several steps between the the last reset event, and the end of integration, otherwise an exception may be thrown during integration. The user can adjust the end date of integration, or the step size of the starter integrator to ensure a sufficient number of steps can be completed before the end of integration.
    
    Implementation details
    
    We define scaled derivatives s :sub:`i` (n) at step n as: \[ \left\{\begin{align} s_1(n) &= h y'_n \text{ for first derivative}\\ s_2(n) &= \frac{h^2}{2} y_n'' \text{ for second derivative}\\ s_3(n) &= \frac{h^3}{6} y_n''' \text{ for third derivative}\\ &\cdots\\ s_k(n) &= \frac{h^k}{k!} y_n^{(k)} \text{ for } k^\mathrm{th} \text{ derivative} \end{align}\right. \]
    
    The definitions above use the classical representation with several previous first derivatives. Lets define \[ q_n = [ s_1(n-1) s_1(n-2) \ldots s_1(n-(k-1)) ]^T \] (we omit the k index in the notation for clarity). With these definitions, Adams-Bashforth methods can be written: \[ \left\{\begin{align} k = 1: & y_{n+1} = y_n + s_1(n) \\ k = 2: & y_{n+1} = y_n + \frac{3}{2} s_1(n) + [ \frac{-1}{2} ] q_n \\ k = 3: & y_{n+1} = y_n + \frac{23}{12} s_1(n) + [ \frac{-16}{12} \frac{5}{12} ] q_n \\ k = 4: & y_{n+1} = y_n + \frac{55}{24} s_1(n) + [ \frac{-59}{24} \frac{37}{24} \frac{-9}{24} ] q_n \\ & \cdots \end{align}\right. \]
    
    Instead of using the classical representation with first derivatives only (y :sub:`n` , s :sub:`1` (n) and q :sub:`n` ), our implementation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same step (y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as: \[ r_n = [ s_2(n), s_3(n) \ldots s_k(n) ]^T \] (here again we omit the k index in the notation for clarity)
    
    Taylor series formulas show that for any index offset i, s :sub:`1` (n-i) can be computed from s :sub:`1` (n), s :sub:`2` (n) ... s :sub:`k` (n), the formula being exact for degree k polynomials. \[ s_1(n-i) = s_1(n) + \sum_{j\gt 0} (j+1) (-i)^j s_{j+1}(n) \] The previous formula can be used with several values for i to compute the transform between classical representation and Nordsieck vector. The transform between r :sub:`n` and q :sub:`n` resulting from the Taylor series formulas above is: \[ q_n = s_1(n) u + P r_n \] where u is the [ 1 1 ... 1 ] :sup:`T` vector and P is the (k-1)×(k-1) matrix built with the \((j+1) (-i)^j\) terms with i being the row number starting from 1 and j being the column number starting from 1: \[ P=\begin{bmatrix} -2 & 3 & -4 & 5 & \ldots \\ -4 & 12 & -32 & 80 & \ldots \\ -6 & 27 & -108 & 405 & \ldots \\ -8 & 48 & -256 & 1280 & \ldots \\ & & \ldots\\ \end{bmatrix} \]
    
    Using the Nordsieck vector has several advantages:
    
      - it greatly simplifies step interpolation as the interpolator mainly applies Taylor series formulas,
      - it simplifies step changes that occur when discrete events that truncate the step are triggered,
      - it allows to extend the methods in order to support adaptive stepsize.
    
    The Nordsieck vector at step n+1 is computed from the Nordsieck vector at step n as follows:
    
      - y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
      - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
      - r :sub:`n+1` = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
    where A is a rows shifting matrix (the lower left part is an identity matrix):
    
            [ 0 0   ...  0 0 | 0 ] [ ---------------+---] [ 1 0   ...  0 0 | 0 ] A = [ 0 1   ...  0 0 | 0 ] [       ...      | 0 ] [ 0 0   ...  1 0 | 0 ] [ 0 0   ...  0 1 | 0 ]
    
    The P :sup:`-1` u vector and the P :sup:`-1` A P matrix do not depend on the state, they only depend on k and therefore are precomputed once for all.
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_AdamsBashforthFieldIntegrator__T], int: int, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_AdamsBashforthFieldIntegrator__T], int: int, double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...

class AdamsBashforthIntegrator(AdamsIntegrator):
    """
    This class implements explicit Adams-Bashforth integrators for Ordinary Differential Equations.
    
    Adams-Bashforth methods (in fact due to Adams alone) are explicit multistep ODE solvers. This implementation is a variation of the classical one: it uses adaptive stepsize to implement error control, whereas classical implementations are fixed step size. The value of state vector at step n+1 is a simple combination of the value at step n and of the derivatives at steps n, n-1, n-2 ... Depending on the number k of previous steps one wants to use for computing the next value, different formulas are available:
    
      - k = 1: y :sub:`n+1` = y :sub:`n` + h y' :sub:`n`
      - k = 2: y :sub:`n+1` = y :sub:`n` + h (3y' :sub:`n` -y' :sub:`n-1` )/2
      - k = 3: y :sub:`n+1` = y :sub:`n` + h (23y' :sub:`n` -16y' :sub:`n-1` +5y' :sub:`n-2` )/12
      - k = 4: y :sub:`n+1` = y :sub:`n` + h (55y' :sub:`n` -59y' :sub:`n-1` +37y' :sub:`n-2` -9y' :sub:`n-3` )/24
      - ...
    
    A k-steps Adams-Bashforth method is of order k.
    
    There must be sufficient time for the setStarterIntegrator to take several steps between the the last reset event, and the end of integration, otherwise an exception may be thrown during integration. The user can adjust the end date of integration, or the step size of the starter integrator to ensure a sufficient number of steps can be completed before the end of integration.
    
    Implementation details
    
    We define scaled derivatives s :sub:`i` (n) at step n as: \[ \left\{\begin{align} s_1(n) &= h y'_n \text{ for first derivative}\\ s_2(n) &= \frac{h^2}{2} y_n'' \text{ for second derivative}\\ s_3(n) &= \frac{h^3}{6} y_n''' \text{ for third derivative}\\ &\cdots\\ s_k(n) &= \frac{h^k}{k!} y_n^{(k)} \text{ for } k^\mathrm{th} \text{ derivative} \end{align}\right. \]
    
    The definitions above use the classical representation with several previous first derivatives. Lets define \[ q_n = [ s_1(n-1) s_1(n-2) \ldots s_1(n-(k-1)) ]^T \] (we omit the k index in the notation for clarity). With these definitions, Adams-Bashforth methods can be written: \[ \left\{\begin{align} k = 1: & y_{n+1} = y_n + s_1(n) \\ k = 2: & y_{n+1} = y_n + \frac{3}{2} s_1(n) + [ \frac{-1}{2} ] q_n \\ k = 3: & y_{n+1} = y_n + \frac{23}{12} s_1(n) + [ \frac{-16}{12} \frac{5}{12} ] q_n \\ k = 4: & y_{n+1} = y_n + \frac{55}{24} s_1(n) + [ \frac{-59}{24} \frac{37}{24} \frac{-9}{24} ] q_n \\ & \cdots \end{align}\right. \]
    
    Instead of using the classical representation with first derivatives only (y :sub:`n` , s :sub:`1` (n) and q :sub:`n` ), our implementation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same step (y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as: \[ r_n = [ s_2(n), s_3(n) \ldots s_k(n) ]^T \] (here again we omit the k index in the notation for clarity)
    
    Taylor series formulas show that for any index offset i, s :sub:`1` (n-i) can be computed from s :sub:`1` (n), s :sub:`2` (n) ... s :sub:`k` (n), the formula being exact for degree k polynomials. \[ s_1(n-i) = s_1(n) + \sum_{j\gt 0} (j+1) (-i)^j s_{j+1}(n) \] The previous formula can be used with several values for i to compute the transform between classical representation and Nordsieck vector. The transform between r :sub:`n` and q :sub:`n` resulting from the Taylor series formulas above is: \[ q_n = s_1(n) u + P r_n \] where u is the [ 1 1 ... 1 ] :sup:`T` vector and P is the (k-1)×(k-1) matrix built with the \((j+1) (-i)^j\) terms with i being the row number starting from 1 and j being the column number starting from 1: \[ P=\begin{bmatrix} -2 & 3 & -4 & 5 & \ldots \\ -4 & 12 & -32 & 80 & \ldots \\ -6 & 27 & -108 & 405 & \ldots \\ -8 & 48 & -256 & 1280 & \ldots \\ & & \ldots\\ \end{bmatrix} \]
    
    Using the Nordsieck vector has several advantages:
    
      - it greatly simplifies step interpolation as the interpolator mainly applies Taylor series formulas,
      - it simplifies step changes that occur when discrete events that truncate the step are triggered,
      - it allows to extend the methods in order to support adaptive stepsize.
    
    The Nordsieck vector at step n+1 is computed from the Nordsieck vector at step n as follows:
    
      - y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
      - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
      - r :sub:`n+1` = (s :sub:`1` (n) - s :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
    where A is a rows shifting matrix (the lower left part is an identity matrix):
    
            [ 0 0   ...  0 0 | 0 ] [ ---------------+---] [ 1 0   ...  0 0 | 0 ] A = [ 0 1   ...  0 0 | 0 ] [       ...      | 0 ] [ 0 0   ...  1 0 | 0 ] [ 0 0   ...  0 1 | 0 ]
    
    The P :sup:`-1` u vector and the P :sup:`-1` A P matrix do not depend on the state, they only depend on k and therefore are precomputed once for all.
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...

_AdamsMoultonFieldIntegrator__T = typing.TypeVar('_AdamsMoultonFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdamsMoultonFieldIntegrator(AdamsFieldIntegrator[_AdamsMoultonFieldIntegrator__T], typing.Generic[_AdamsMoultonFieldIntegrator__T]):
    """
    This class implements implicit Adams-Moulton integrators for Ordinary Differential Equations.
    
    Adams-Moulton methods (in fact due to Adams alone) are implicit multistep ODE solvers. This implementation is a variation of the classical one: it uses adaptive stepsize to implement error control, whereas classical implementations are fixed step size. The value of state vector at step n+1 is a simple combination of the value at step n and of the derivatives at steps n+1, n, n-1 ... Since y' :sub:`n+1` is needed to compute y :sub:`n+1` , another method must be used to compute a first estimate of y :sub:`n+1` , then compute y' :sub:`n+1` , then compute a final estimate of y :sub:`n+1` using the following formulas. Depending on the number k of previous steps one wants to use for computing the next value, different formulas are available for the final estimate:
    
      - k = 1: y :sub:`n+1` = y :sub:`n` + h y' :sub:`n+1`
      - k = 2: y :sub:`n+1` = y :sub:`n` + h (y' :sub:`n+1` +y' :sub:`n` )/2
      - k = 3: y :sub:`n+1` = y :sub:`n` + h (5y' :sub:`n+1` +8y' :sub:`n` -y' :sub:`n-1` )/12
      - k = 4: y :sub:`n+1` = y :sub:`n` + h (9y' :sub:`n+1` +19y' :sub:`n` -5y' :sub:`n-1` +y' :sub:`n-2` )/24
      - ...
    
    A k-steps Adams-Moulton method is of order k+1.
    
    There must be sufficient time for the setStarterIntegrator to take several steps between the the last reset event, and the end of integration, otherwise an exception may be thrown during integration. The user can adjust the end date of integration, or the step size of the starter integrator to ensure a sufficient number of steps can be completed before the end of integration.
    
    Implementation details
    
    We define scaled derivatives s :sub:`i` (n) at step n as: \[ \left\{\begin{align} s_1(n) &= h y'_n \text{ for first derivative}\\ s_2(n) &= \frac{h^2}{2} y_n'' \text{ for second derivative}\\ s_3(n) &= \frac{h^3}{6} y_n''' \text{ for third derivative}\\ &\cdots\\ s_k(n) &= \frac{h^k}{k!} y_n^{(k)} \text{ for } k^\mathrm{th} \text{ derivative} \end{align}\right. \]
    
    The definitions above use the classical representation with several previous first derivatives. Lets define \[ q_n = [ s_1(n-1) s_1(n-2) \ldots s_1(n-(k-1)) ]^T \] (we omit the k index in the notation for clarity). With these definitions, Adams-Moulton methods can be written:
    
      - k = 1: y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n+1)
      - k = 2: y :sub:`n+1` = y :sub:`n` + 1/2 s :sub:`1` (n+1) + [ 1/2 ] q :sub:`n+1`
      - k = 3: y :sub:`n+1` = y :sub:`n` + 5/12 s :sub:`1` (n+1) + [ 8/12 -1/12 ] q :sub:`n+1`
      - k = 4: y :sub:`n+1` = y :sub:`n` + 9/24 s :sub:`1` (n+1) + [ 19/24 -5/24 1/24 ] q :sub:`n+1`
      - ...
    
    Instead of using the classical representation with first derivatives only (y :sub:`n` , s :sub:`1` (n+1) and q :sub:`n+1` ), our implementation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same step (y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as: \[ r_n = [ s_2(n), s_3(n) \ldots s_k(n) ]^T \] (here again we omit the k index in the notation for clarity)
    
    Taylor series formulas show that for any index offset i, s :sub:`1` (n-i) can be computed from s :sub:`1` (n), s :sub:`2` (n) ... s :sub:`k` (n), the formula being exact for degree k polynomials. \[ s_1(n-i) = s_1(n) + \sum_{j\gt 0} (j+1) (-i)^j s_{j+1}(n) \] The previous formula can be used with several values for i to compute the transform between classical representation and Nordsieck vector. The transform between r :sub:`n` and q :sub:`n` resulting from the Taylor series formulas above is: \[ q_n = s_1(n) u + P r_n \] where u is the [ 1 1 ... 1 ] :sup:`T` vector and P is the (k-1)×(k-1) matrix built with the \((j+1) (-i)^j\) terms with i being the row number starting from 1 and j being the column number starting from 1: \[ P=\begin{bmatrix} -2 & 3 & -4 & 5 & \ldots \\ -4 & 12 & -32 & 80 & \ldots \\ -6 & 27 & -108 & 405 & \ldots \\ -8 & 48 & -256 & 1280 & \ldots \\ & & \ldots\\ \end{bmatrix} \]
    
    Using the Nordsieck vector has several advantages:
    
      - it greatly simplifies step interpolation as the interpolator mainly applies Taylor series formulas,
      - it simplifies step changes that occur when discrete events that truncate the step are triggered,
      - it allows to extend the methods in order to support adaptive stepsize.
    
    The predicted Nordsieck vector at step n+1 is computed from the Nordsieck vector at step n as follows:
    
      - Y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
      - S :sub:`1` (n+1) = h f(t :sub:`n+1` , Y :sub:`n+1` )
      - R :sub:`n+1` = (s :sub:`1` (n) - S :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
    where A is a rows shifting matrix (the lower left part is an identity matrix):
    
            [ 0 0   ...  0 0 | 0 ] [ ---------------+---] [ 1 0   ...  0 0 | 0 ] A = [ 0 1   ...  0 0 | 0 ] [       ...      | 0 ] [ 0 0   ...  1 0 | 0 ] [ 0 0   ...  0 1 | 0 ] From this predicted vector, the corrected vector is computed as follows:
    
      - y :sub:`n+1` = y :sub:`n` + S :sub:`1` (n+1) + [ -1 +1 -1 +1 ... ±1 ] r :sub:`n+1`
      - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
      - r :sub:`n+1` = R :sub:`n+1` + (s :sub:`1` (n+1) - S :sub:`1` (n+1)) P :sup:`-1` u
    
    where the upper case Y :sub:`n+1` , S :sub:`1` (n+1) and R :sub:`n+1` represent the predicted states whereas the lower case y :sub:`n+1` , s :sub:`n+1` and r :sub:`n+1` represent the corrected states.
    
    The P :sup:`-1` u vector and the P :sup:`-1` A P matrix do not depend on the state, they only depend on k and therefore are precomputed once for all.
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_AdamsMoultonFieldIntegrator__T], int: int, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_AdamsMoultonFieldIntegrator__T], int: int, double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...

class AdamsMoultonIntegrator(AdamsIntegrator):
    """
    This class implements implicit Adams-Moulton integrators for Ordinary Differential Equations.
    
    Adams-Moulton methods (in fact due to Adams alone) are implicit multistep ODE solvers. This implementation is a variation of the classical one: it uses adaptive stepsize to implement error control, whereas classical implementations are fixed step size. The value of state vector at step n+1 is a simple combination of the value at step n and of the derivatives at steps n+1, n, n-1 ... Since y' :sub:`n+1` is needed to compute y :sub:`n+1` , another method must be used to compute a first estimate of y :sub:`n+1` , then compute y' :sub:`n+1` , then compute a final estimate of y :sub:`n+1` using the following formulas. Depending on the number k of previous steps one wants to use for computing the next value, different formulas are available for the final estimate:
    
      - k = 1: y :sub:`n+1` = y :sub:`n` + h y' :sub:`n+1`
      - k = 2: y :sub:`n+1` = y :sub:`n` + h (y' :sub:`n+1` +y' :sub:`n` )/2
      - k = 3: y :sub:`n+1` = y :sub:`n` + h (5y' :sub:`n+1` +8y' :sub:`n` -y' :sub:`n-1` )/12
      - k = 4: y :sub:`n+1` = y :sub:`n` + h (9y' :sub:`n+1` +19y' :sub:`n` -5y' :sub:`n-1` +y' :sub:`n-2` )/24
      - ...
    
    A k-steps Adams-Moulton method is of order k+1.
    
    There must be sufficient time for the setStarterIntegrator to take several steps between the the last reset event, and the end of integration, otherwise an exception may be thrown during integration. The user can adjust the end date of integration, or the step size of the starter integrator to ensure a sufficient number of steps can be completed before the end of integration.
    
    Implementation details
    
    We define scaled derivatives s :sub:`i` (n) at step n as: \[ \left\{\begin{align} s_1(n) &= h y'_n \text{ for first derivative}\\ s_2(n) &= \frac{h^2}{2} y_n'' \text{ for second derivative}\\ s_3(n) &= \frac{h^3}{6} y_n''' \text{ for third derivative}\\ &\cdots\\ s_k(n) &= \frac{h^k}{k!} y_n^{(k)} \text{ for } k^\mathrm{th} \text{ derivative} \end{align}\right. \]
    
    The definitions above use the classical representation with several previous first derivatives. Lets define \[ q_n = [ s_1(n-1) s_1(n-2) \ldots s_1(n-(k-1)) ]^T \] (we omit the k index in the notation for clarity). With these definitions, Adams-Moulton methods can be written:
    
      - k = 1: y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n+1)
      - k = 2: y :sub:`n+1` = y :sub:`n` + 1/2 s :sub:`1` (n+1) + [ 1/2 ] q :sub:`n+1`
      - k = 3: y :sub:`n+1` = y :sub:`n` + 5/12 s :sub:`1` (n+1) + [ 8/12 -1/12 ] q :sub:`n+1`
      - k = 4: y :sub:`n+1` = y :sub:`n` + 9/24 s :sub:`1` (n+1) + [ 19/24 -5/24 1/24 ] q :sub:`n+1`
      - ...
    
    Instead of using the classical representation with first derivatives only (y :sub:`n` , s :sub:`1` (n+1) and q :sub:`n+1` ), our implementation uses the Nordsieck vector with higher degrees scaled derivatives all taken at the same step (y :sub:`n` , s :sub:`1` (n) and r :sub:`n` ) where r :sub:`n` is defined as: \[ r_n = [ s_2(n), s_3(n) \ldots s_k(n) ]^T \] (here again we omit the k index in the notation for clarity)
    
    Taylor series formulas show that for any index offset i, s :sub:`1` (n-i) can be computed from s :sub:`1` (n), s :sub:`2` (n) ... s :sub:`k` (n), the formula being exact for degree k polynomials. \[ s_1(n-i) = s_1(n) + \sum_{j\gt 0} (j+1) (-i)^j s_{j+1}(n) \] The previous formula can be used with several values for i to compute the transform between classical representation and Nordsieck vector. The transform between r :sub:`n` and q :sub:`n` resulting from the Taylor series formulas above is: \[ q_n = s_1(n) u + P r_n \] where u is the [ 1 1 ... 1 ] :sup:`T` vector and P is the (k-1)×(k-1) matrix built with the \((j+1) (-i)^j\) terms with i being the row number starting from 1 and j being the column number starting from 1: \[ P=\begin{bmatrix} -2 & 3 & -4 & 5 & \ldots \\ -4 & 12 & -32 & 80 & \ldots \\ -6 & 27 & -108 & 405 & \ldots \\ -8 & 48 & -256 & 1280 & \ldots \\ & & \ldots\\ \end{bmatrix} \]
    
    Using the Nordsieck vector has several advantages:
    
      - it greatly simplifies step interpolation as the interpolator mainly applies Taylor series formulas,
      - it simplifies step changes that occur when discrete events that truncate the step are triggered,
      - it allows to extend the methods in order to support adaptive stepsize.
    
    The predicted Nordsieck vector at step n+1 is computed from the Nordsieck vector at step n as follows:
    
      - Y :sub:`n+1` = y :sub:`n` + s :sub:`1` (n) + u :sup:`T` r :sub:`n`
      - S :sub:`1` (n+1) = h f(t :sub:`n+1` , Y :sub:`n+1` )
      - R :sub:`n+1` = (s :sub:`1` (n) - S :sub:`1` (n+1)) P :sup:`-1` u + P :sup:`-1` A P r :sub:`n`
    
    where A is a rows shifting matrix (the lower left part is an identity matrix):
    
            [ 0 0   ...  0 0 | 0 ] [ ---------------+---] [ 1 0   ...  0 0 | 0 ] A = [ 0 1   ...  0 0 | 0 ] [       ...      | 0 ] [ 0 0   ...  1 0 | 0 ] [ 0 0   ...  0 1 | 0 ] From this predicted vector, the corrected vector is computed as follows:
    
      - y :sub:`n+1` = y :sub:`n` + S :sub:`1` (n+1) + [ -1 +1 -1 +1 ... ±1 ] r :sub:`n+1`
      - s :sub:`1` (n+1) = h f(t :sub:`n+1` , y :sub:`n+1` )
      - r :sub:`n+1` = R :sub:`n+1` + (s :sub:`1` (n+1) - S :sub:`1` (n+1)) P :sup:`-1` u
    
    where the upper case Y :sub:`n+1` , S :sub:`1` (n+1) and R :sub:`n+1` represent the predicted states whereas the lower case y :sub:`n+1` , s :sub:`n+1` and r :sub:`n+1` represent the corrected states.
    
    The P :sup:`-1` u vector and the P :sup:`-1` A P matrix do not depend on the state, they only depend on k and therefore are precomputed once for all.
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...

class ExplicitRungeKuttaIntegrator(ButcherArrayProvider, org.hipparchus.ode.ODEIntegrator):
    """
    This interface implements the part of Runge-Kutta integrators for Ordinary Differential Equations common to fixed- and adaptive steps.
    
    These methods are explicit Runge-Kutta methods, their Butcher arrays are as follows :
    
        0  | c2  | a21 c3  | a31  a32 ... |        ... cs  | as1  as2  ...  ass-1 |-------------------------- |  b1   b2  ...   bs-1  bs
    
    Since:
        3.1
    
          - ButcherArrayProvider
          - FixedStepRungeKuttaIntegrator
          - EmbeddedRungeKuttaIntegrator
    """
    @staticmethod
    def applyExternalButcherWeights(y0: typing.Union[typing.List[float], jpype.JArray], yDotK: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], h: float, b: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Apply external weights of Butcher array, assuming internal ones have been applied.
        
        Parameters:
            y0 (double[]): initial value of the state vector at t0
            yDotK (double[][]): output of stages
            h (double): step size
            b (double[]): external weights of Butcher array
        
        Returns:
            state vector
        
        
        """
        ...
    @staticmethod
    def applyInternalButcherWeights(equations: org.hipparchus.ode.ExpandableODE, t0: float, y0: typing.Union[typing.List[float], jpype.JArray], h: float, a: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], c: typing.Union[typing.List[float], jpype.JArray], yDotK: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
        Apply internal weights of Butcher array, with corresponding times.
        
        Parameters:
            equations (ExpandableODE): differential equations to integrate
            t0 (double): initial time
            y0 (double[]): initial value of the state vector at t0
            h (double): step size
            a (double[][]): internal weights of Butcher array
            c (double[]): times of Butcher array
            yDotK (double[][]): array where to store result
        
        
        """
        ...
    def getNumberOfStages(self) -> int:
        """
        Getter for the number of stages corresponding to the Butcher array.
        
        Returns:
            number of stages
        
        
        """
        ...
    def singleStep(self, equations: org.hipparchus.ode.OrdinaryDifferentialEquation, t0: float, y0: typing.Union[typing.List[float], jpype.JArray], t: float) -> typing.MutableSequence[float]:
        """
        Fast computation of a single step of ODE integration.
        
        This method is intended for the limited use case of very fast computation of only one step without using any of the rich features of general integrators that may take some time to set up (i.e. no step handlers, no events handlers, no additional states, no interpolators, no error control, no evaluations count, no sanity checks ...). It handles the strict minimum of computation, so it can be embedded in outer loops.
        
        This method is not used at all by the integrate method. It also completely ignores the step set at construction time, and uses only a single step to go from t0 to t.
        
        As this method does not use any of the state-dependent features of the integrator, it should be reasonably thread-safe if and only if the provided differential equations are themselves thread-safe.
        
        Parameters:
            equations (OrdinaryDifferentialEquation): differential equations to integrate
            t0 (double): initial time
            y0 (double[]): initial value of the state vector at t0
            t (double): target time for the integration (can be set to a value smaller than t0 for backward integration)
        
        Returns:
            state vector at t
        
        
        """
        ...

_FieldExplicitRungeKuttaIntegrator__T = typing.TypeVar('_FieldExplicitRungeKuttaIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldExplicitRungeKuttaIntegrator(FieldButcherArrayProvider[_FieldExplicitRungeKuttaIntegrator__T], org.hipparchus.ode.FieldODEIntegrator[_FieldExplicitRungeKuttaIntegrator__T], typing.Generic[_FieldExplicitRungeKuttaIntegrator__T]):
    """
    This interface implements the part of Runge-Kutta Field integrators for Ordinary Differential Equations common to fixed- and adaptive steps.
    
    These methods are explicit Runge-Kutta methods, their Butcher arrays are as follows :
    
        0  | c2  | a21 c3  | a31  a32 ... |        ... cs  | as1  as2  ...  ass-1 |-------------------------- |  b1   b2  ...   bs-1  bs
    
    Since:
        3.1
    
          - FieldButcherArrayProvider
          - FixedStepRungeKuttaFieldIntegrator
          - EmbeddedRungeKuttaFieldIntegrator
    """
    _applyExternalButcherWeights_0__T = typing.TypeVar('_applyExternalButcherWeights_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _applyExternalButcherWeights_1__T = typing.TypeVar('_applyExternalButcherWeights_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def applyExternalButcherWeights(tArray: typing.Union[typing.List[_applyExternalButcherWeights_0__T], jpype.JArray], tArray2: typing.Union[typing.List[typing.MutableSequence[_applyExternalButcherWeights_0__T]], jpype.JArray], t3: _applyExternalButcherWeights_0__T, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[_applyExternalButcherWeights_0__T]:
        """
        Apply external weights of Butcher array, assuming internal ones have been applied.
        
        Parameters:
            y0 (T[]): initial value of the state vector at t0
            yDotK (T[][]): output of stages
            h (T): step size
            b (T[]): external weights of Butcher array
        
        Returns:
            state vector
        
        Apply external weights of Butcher array, assuming internal ones have been applied. Version with real Butcher array (non-Field version).
        
        Parameters:
            y0 (T[]): initial value of the state vector at t0
            yDotK (T[][]): output of stages
            h (T): step size
            b (double[]): external weights of Butcher array
        
        Returns:
            state vector
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def applyExternalButcherWeights(tArray: typing.Union[typing.List[_applyExternalButcherWeights_1__T], jpype.JArray], tArray2: typing.Union[typing.List[typing.MutableSequence[_applyExternalButcherWeights_1__T]], jpype.JArray], t3: _applyExternalButcherWeights_1__T, tArray3: typing.Union[typing.List[_applyExternalButcherWeights_1__T], jpype.JArray]) -> typing.MutableSequence[_applyExternalButcherWeights_1__T]: ...
    _applyInternalButcherWeights_0__T = typing.TypeVar('_applyInternalButcherWeights_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _applyInternalButcherWeights_1__T = typing.TypeVar('_applyInternalButcherWeights_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def applyInternalButcherWeights(fieldExpandableODE: org.hipparchus.ode.FieldExpandableODE[_applyInternalButcherWeights_0__T], t: _applyInternalButcherWeights_0__T, tArray: typing.Union[typing.List[_applyInternalButcherWeights_0__T], jpype.JArray], t3: _applyInternalButcherWeights_0__T, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], tArray2: typing.Union[typing.List[typing.MutableSequence[_applyInternalButcherWeights_0__T]], jpype.JArray]) -> None:
        """
        Apply internal weights of Butcher array, with corresponding times.
        
        Parameters:
            equations (FieldExpandableODE<T> equations): differential equations to integrate
            t0 (T): initial time
            y0 (T[]): initial value of the state vector at t0
            h (T): step size
            a (T[][]): internal weights of Butcher array
            c (T[]): times of Butcher array
            yDotK (T[][]): array where to store result
        
        Apply internal weights of Butcher array, with corresponding times. Version with real Butcher array (non-Field).
        
        Parameters:
            equations (FieldExpandableODE<T> equations): differential equations to integrate
            t0 (T): initial time
            y0 (T[]): initial value of the state vector at t0
            h (T): step size
            a (double[][]): internal weights of Butcher array
            c (double[]): times of Butcher array
            yDotK (T[][]): array where to store result
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def applyInternalButcherWeights(fieldExpandableODE: org.hipparchus.ode.FieldExpandableODE[_applyInternalButcherWeights_1__T], t: _applyInternalButcherWeights_1__T, tArray: typing.Union[typing.List[_applyInternalButcherWeights_1__T], jpype.JArray], t3: _applyInternalButcherWeights_1__T, tArray2: typing.Union[typing.List[typing.MutableSequence[_applyInternalButcherWeights_1__T]], jpype.JArray], tArray3: typing.Union[typing.List[_applyInternalButcherWeights_1__T], jpype.JArray], tArray4: typing.Union[typing.List[typing.MutableSequence[_applyInternalButcherWeights_1__T]], jpype.JArray]) -> None: ...
    _fraction_0__T = typing.TypeVar('_fraction_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _fraction_1__T = typing.TypeVar('_fraction_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def fraction(field: org.hipparchus.Field[_fraction_0__T], double: float, double2: float) -> _fraction_0__T:
        """
        Create a fraction from integers.
        
        Parameters:
            field (hipparchus<T> field): field to which elements belong
            p (int): numerator
            q (int): denominator
        
        Returns:
            p/q computed in the instance field
        
        Create a fraction from doubles.
        
        Parameters:
            field (hipparchus<T> field): field to which elements belong
            p (double): numerator
            q (double): denominator
        
        Returns:
            p/q computed in the instance field
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def fraction(field: org.hipparchus.Field[_fraction_1__T], int: int, int2: int) -> _fraction_1__T: ...
    def getNumberOfStages(self) -> int:
        """
        Getter for the number of stages corresponding to the Butcher array.
        
        Returns:
            number of stages
        
        
        """
        ...
    def getRealA(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the internal weights from Butcher array (without the first empty row). Real version (non-Field).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getRealB(self) -> typing.MutableSequence[float]:
        """
        Get the external weights for the high order method from Butcher array. Real version (non-Field).
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getRealC(self) -> typing.MutableSequence[float]:
        """
        Get the time steps from Butcher array (without the first zero). Real version (non-Field).
        
        Returns:
            time steps from Butcher array (without the first zero).
        
        
        """
        ...
    def isUsingFieldCoefficients(self) -> bool:
        """
        Getter for the flag between real or Field coefficients in the Butcher array.
        
        Returns:
            flag
        
        
        """
        ...
    def singleStep(self, equations: org.hipparchus.ode.FieldOrdinaryDifferentialEquation[_FieldExplicitRungeKuttaIntegrator__T], t0: _FieldExplicitRungeKuttaIntegrator__T, y0: typing.Union[typing.List[_FieldExplicitRungeKuttaIntegrator__T], jpype.JArray], t: _FieldExplicitRungeKuttaIntegrator__T) -> typing.MutableSequence[_FieldExplicitRungeKuttaIntegrator__T]:
        """
        Fast computation of a single step of ODE integration.
        
        This method is intended for the limited use case of very fast computation of only one step without using any of the rich features of general integrators that may take some time to set up (i.e. no step handlers, no events handlers, no additional states, no interpolators, no error control, no evaluations count, no sanity checks ...). It handles the strict minimum of computation, so it can be embedded in outer loops.
        
        This method is not used at all by the integrate method. It also completely ignores the step set at construction time, and uses only a single step to go from t0 to t.
        
        As this method does not use any of the state-dependent features of the integrator, it should be reasonably thread-safe if and only if the provided differential equations are themselves thread-safe.
        
        Parameters:
            equations (FieldOrdinaryDifferentialEquation<FieldExplicitRungeKuttaIntegrator> equations): differential equations to integrate
            t0 (FieldExplicitRungeKuttaIntegrator): initial time
            y0 (FieldExplicitRungeKuttaIntegrator[]): initial value of the state vector at t0
            t (FieldExplicitRungeKuttaIntegrator): target time for the integration (can be set to a value smaller than t0 for backward integration)
        
        Returns:
            state vector at t
        
        
        """
        ...

class GraggBulirschStoerIntegrator(AdaptiveStepsizeIntegrator):
    """
    This class implements a Gragg-Bulirsch-Stoer integrator for Ordinary Differential Equations.
    
    The Gragg-Bulirsch-Stoer algorithm is one of the most efficient ones currently available for smooth problems. It uses Richardson extrapolation to estimate what would be the solution if the step size could be decreased down to zero.
    
    This method changes both the step size and the order during integration, in order to minimize computation cost. It is particularly well suited when a very high precision is needed. The limit where this method becomes more efficient than high-order embedded Runge-Kutta methods like DormandPrince853Integrator depends on the problem. Results given in the Hairer, Norsett and Wanner book show for example that this limit occurs for accuracy around 1e-6 when integrating Saltzam-Lorenz equations (the authors note this problem is extremely sensitive to the errors in the first integration steps), and around 1e-11 for a two dimensional celestial mechanics problems with seven bodies (pleiades problem, involving quasi-collisions for which automatic step size control is essential).
    
    This implementation is basically a reimplementation in Java of the `odex <http://www.unige.ch/math/folks/hairer/prog/nonstiff/odex.f>` fortran code by E. Hairer and G. Wanner. The redistribution policy for this code is available `here <http://www.unige.ch/~hairer/prog/licence.txt>`, for convenience, it is reproduced below.
    
        Copyright (c) 2004, Ernst Hairer
    
        Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
    
          - Redistributions of source code must retain the above copyright notice, this list of conditions and the following
            disclaimer.
          - Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
            disclaimer in the documentation and/or other materials provided with the distribution.
    
        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def integrate(self, ordinaryDifferentialEquation: org.hipparchus.ode.OrdinaryDifferentialEquation, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...
    @typing.overload
    def integrate(self, expandableODE: org.hipparchus.ode.ExpandableODE, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...
    def setControlFactors(self, control1: float, control2: float, control3: float, control4: float) -> None:
        """
        Set the step size control factors.
        
        The new step size hNew is computed from the old one h by:
        
         hNew = h * stepControl2 / (err/stepControl1)^(1/(2k + 1))
        
        where err is the scaled error and k the iteration number of the extrapolation scheme (counting from 0). The default values are 0.65 for stepControl1 and 0.94 for stepControl2.
        
        The step size is subject to the restriction:
        
         stepControl3^(1/(2k + 1))/stepControl4 <= hNew/h <= 1/stepControl3^(1/(2k + 1))
        
        The default values are 0.02 for stepControl3 and 4.0 for stepControl4.
        
        Parameters:
            control1 (double): first stepsize control factor (the factor is reset to default if lower than 0.0001 or greater than 0.9999)
            control2 (double): second stepsize control factor (the factor is reset to default if lower than 0.0001 or greater than 0.9999)
            control3 (double): third stepsize control factor (the factor is reset to default if lower than 0.0001 or greater than 0.9999)
            control4 (double): fourth stepsize control factor (the factor is reset to default if lower than 1.0001 or greater than 999.9)
        
        
        """
        ...
    def setInterpolationControl(self, useInterpolationErrorForControl: bool, mudifControlParameter: int) -> None:
        """
        Set the interpolation order control parameter. The interpolation order for dense output is 2k - mudif + 1. The default value for mudif is 4 and the interpolation error is used in stepsize control by default.
        
        Parameters:
            useInterpolationErrorForControl (boolean): if true, interpolation error is used for stepsize control
            mudifControlParameter (int): interpolation order control parameter (the parameter is reset to default if <= 0 or >= 7)
        
        
        """
        ...
    def setOrderControl(self, maximalOrder: int, control1: float, control2: float) -> None:
        """
        Set the order control parameters.
        
        The Gragg-Bulirsch-Stoer method changes both the step size and the order during integration, in order to minimize computation cost. Each extrapolation step increases the order by 2, so the maximal order that will be used is always even, it is twice the maximal number of columns in the extrapolation table.
        
         order is decreased if w(k - 1) <= w(k)     * orderControl1 order is increased if w(k)     <= w(k - 1) * orderControl2
        
        where w is the table of work per unit step for each order (number of function calls divided by the step length), and k is the current order.
        
        The default maximal order after construction is 18 (i.e. the maximal number of columns is 9). The default values are 0.8 for orderControl1 and 0.9 for orderControl2.
        
        Parameters:
            maximalOrder (int): maximal order in the extrapolation table (the maximal order is reset to default if order <= 6 or odd)
            control1 (double): first order control factor (the factor is reset to default if lower than 0.0001 or greater than 0.9999)
            control2 (double): second order control factor (the factor is reset to default if lower than 0.0001 or greater than 0.9999)
        
        
        """
        ...
    def setStabilityCheck(self, performStabilityCheck: bool, maxNumIter: int, maxNumChecks: int, stepsizeReductionFactor: float) -> None:
        """
        Set the stability check controls.
        
        The stability check is performed on the first few iterations of the extrapolation scheme. If this test fails, the step is rejected and the stepsize is reduced.
        
        By default, the test is performed, at most during two iterations at each step, and at most once for each of these iterations. The default stepsize reduction factor is 0.5.
        
        Parameters:
            performStabilityCheck (boolean): if true, stability check will be performed, if false, the check will be skipped
            maxNumIter (int): maximal number of iterations for which checks are performed (the number of iterations is reset to default if negative or
                null)
            maxNumChecks (int): maximal number of checks for each iteration (the number of checks is reset to default if negative or null)
            stepsizeReductionFactor (double): stepsize reduction factor in case of failure (the factor is reset to default if lower than 0.0001 or greater than
                0.9999)
        
        
        """
        ...

_EmbeddedRungeKuttaFieldIntegrator__T = typing.TypeVar('_EmbeddedRungeKuttaFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class EmbeddedRungeKuttaFieldIntegrator(AdaptiveStepsizeFieldIntegrator[_EmbeddedRungeKuttaFieldIntegrator__T], FieldExplicitRungeKuttaIntegrator[_EmbeddedRungeKuttaFieldIntegrator__T], typing.Generic[_EmbeddedRungeKuttaFieldIntegrator__T]):
    """
    implements FieldExplicitRungeKuttaIntegrator<T>
    
    This class implements the common part of all embedded Runge-Kutta integrators for Ordinary Differential Equations.
    
    These methods are embedded explicit Runge-Kutta methods with two sets of coefficients allowing to estimate the error, their Butcher arrays are as follows :
    
        0  | c2  | a21 c3  | a31  a32 ... |        ... cs  | as1  as2  ...  ass-1 |-------------------------- |  b1   b2  ...   bs-1  bs |  b'1  b'2 ...   b's-1 b's
    
    In fact, we rather use the array defined by ej = bj - b'j to compute directly the error rather than computing two estimates and then comparing them.
    
    Some methods are qualified as fsal (first same as last) methods. This means the last evaluation of the derivatives in one step is the same as the first in the next step. Then, this evaluation can be reused from one step to the next one and the cost of such a method is really s-1 evaluations despite the method still has s stages. This behaviour is true only for successful steps, if the step is rejected after the error estimation phase, no evaluation is saved. For an fsal method, we have cs = 1 and asi = bi for all i.
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
    def getNumberOfStages(self) -> int:
        """
        Getter for the number of stages corresponding to the Butcher array.
        
        Specified by: getNumberOfStages in interface FieldExplicitRungeKuttaIntegrator
        
        Returns:
            number of stages
        
        
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
    def integrate(self, equations: org.hipparchus.ode.FieldExpandableODE[_EmbeddedRungeKuttaFieldIntegrator__T], initialState: org.hipparchus.ode.FieldODEState[_EmbeddedRungeKuttaFieldIntegrator__T], finalTime: _EmbeddedRungeKuttaFieldIntegrator__T) -> org.hipparchus.ode.FieldODEStateAndDerivative[_EmbeddedRungeKuttaFieldIntegrator__T]:
        """
        Integrate the differential equations up to the given time.
        
        This method solves an Initial Value Problem (IVP).
        
        Since this method stores some internal state variables made available in its public interface during integration (getCurrentSignedStepsize), it is not thread-safe.
        
        Specified by: integrate in interface FieldODEIntegrator
        
        Parameters:
            equations (FieldExpandableODE<EmbeddedRungeKuttaFieldIntegrator> equations): differential equations to integrate
            initialState (FieldODEState<EmbeddedRungeKuttaFieldIntegrator> initialState): initial state (time, primary and secondary state vectors)
            finalTime (EmbeddedRungeKuttaFieldIntegrator): target time for the integration (can be set to a value smaller than t0 for backward integration)
        
        Returns:
            final state, its time will be the same as finalTime if integration reached its target, but may be different if
            some FieldODEEventHandler stops it at some point.
        
        Raises:
            hipparchus: if integration step is too small
            hipparchus: if the location of an event cannot be bracketed
            hipparchus: if the number of functions evaluations is exceeded
        
        
        """
        ...
    def isUsingFieldCoefficients(self) -> bool:
        """
        Getter for the flag between real or Field coefficients in the Butcher array.
        
        Specified by: isUsingFieldCoefficients in interface FieldExplicitRungeKuttaIntegrator
        
        Returns:
            flag
        
        
        """
        ...
    def setMaxGrowth(self, maxGrowth: _EmbeddedRungeKuttaFieldIntegrator__T) -> None:
        """
        Set the maximal growth factor for stepsize control.
        
        Parameters:
            maxGrowth (EmbeddedRungeKuttaFieldIntegrator): maximal growth factor
        
        
        """
        ...
    def setMinReduction(self, minReduction: _EmbeddedRungeKuttaFieldIntegrator__T) -> None:
        """
        Set the minimal reduction factor for stepsize control.
        
        Parameters:
            minReduction (EmbeddedRungeKuttaFieldIntegrator): minimal reduction factor
        
        
        """
        ...
    def setSafety(self, safety: _EmbeddedRungeKuttaFieldIntegrator__T) -> None:
        """
        Set the safety factor for stepsize control.
        
        Parameters:
            safety (EmbeddedRungeKuttaFieldIntegrator): safety factor
        
        
        """
        ...
    def setUsingFieldCoefficients(self, usingFieldCoefficients: bool) -> None:
        """
        Setter for the flag between real or Field coefficients in the Butcher array.
        
        Parameters:
            usingFieldCoefficients (boolean): new value for flag
        
        
        """
        ...

class EmbeddedRungeKuttaIntegrator(AdaptiveStepsizeIntegrator, ExplicitRungeKuttaIntegrator):
    """
    implements ExplicitRungeKuttaIntegrator
    
    This class implements the common part of all embedded Runge-Kutta integrators for Ordinary Differential Equations.
    
    These methods are embedded explicit Runge-Kutta methods with two sets of coefficients allowing to estimate the error, their Butcher arrays are as follows :
    
        0  | c2  | a21 c3  | a31  a32 ... |        ... cs  | as1  as2  ...  ass-1 |-------------------------- |  b1   b2  ...   bs-1  bs |  b'1  b'2 ...   b's-1 b's
    
    In fact, we rather use the array defined by ej = bj - b'j to compute directly the error rather than computing two estimates and then comparing them.
    
    Some methods are qualified as fsal (first same as last) methods. This means the last evaluation of the derivatives in one step is the same as the first in the next step. Then, this evaluation can be reused from one step to the next one and the cost of such a method is really s-1 evaluations despite the method still has s stages. This behaviour is true only for successful steps, if the step is rejected after the error estimation phase, no evaluation is saved. For an fsal method, we have cs = 1 and asi = bi for all i.
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

_FixedStepRungeKuttaFieldIntegrator__T = typing.TypeVar('_FixedStepRungeKuttaFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FixedStepRungeKuttaFieldIntegrator(org.hipparchus.ode.AbstractFieldIntegrator[_FixedStepRungeKuttaFieldIntegrator__T], FieldExplicitRungeKuttaIntegrator[_FixedStepRungeKuttaFieldIntegrator__T], typing.Generic[_FixedStepRungeKuttaFieldIntegrator__T]):
    """
    implements FieldExplicitRungeKuttaIntegrator<T>
    
    This class implements the common part of all fixed step Runge-Kutta integrators for Ordinary Differential Equations.
    
    These methods are explicit Runge-Kutta methods, their Butcher arrays are as follows :
    
        0  | c2  | a21 c3  | a31  a32 ... |        ... cs  | as1  as2  ...  ass-1 |-------------------------- |  b1   b2  ...   bs-1  bs
    
          - EulerFieldIntegrator
          - ClassicalRungeKuttaFieldIntegrator
          - GillFieldIntegrator
          - MidpointFieldIntegrator
    """
    def getDefaultStep(self) -> _FixedStepRungeKuttaFieldIntegrator__T:
        """
        Getter for the default, positive step-size assigned at constructor level.
        
        Returns:
            step
        
        
        """
        ...
    def getNumberOfStages(self) -> int:
        """
        Getter for the number of stages corresponding to the Butcher array.
        
        Specified by: getNumberOfStages in interface FieldExplicitRungeKuttaIntegrator
        
        Returns:
            number of stages
        
        
        """
        ...
    def integrate(self, equations: org.hipparchus.ode.FieldExpandableODE[_FixedStepRungeKuttaFieldIntegrator__T], initialState: org.hipparchus.ode.FieldODEState[_FixedStepRungeKuttaFieldIntegrator__T], finalTime: _FixedStepRungeKuttaFieldIntegrator__T) -> org.hipparchus.ode.FieldODEStateAndDerivative[_FixedStepRungeKuttaFieldIntegrator__T]:
        """
        Integrate the differential equations up to the given time.
        
        This method solves an Initial Value Problem (IVP).
        
        Since this method stores some internal state variables made available in its public interface during integration (getCurrentSignedStepsize), it is not thread-safe.
        
        Specified by: integrate in interface FieldODEIntegrator
        
        Parameters:
            equations (FieldExpandableODE<FixedStepRungeKuttaFieldIntegrator> equations): differential equations to integrate
            initialState (FieldODEState<FixedStepRungeKuttaFieldIntegrator> initialState): initial state (time, primary and secondary state vectors)
            finalTime (FixedStepRungeKuttaFieldIntegrator): target time for the integration (can be set to a value smaller than t0 for backward integration)
        
        Returns:
            final state, its time will be the same as finalTime if integration reached its target, but may be different if
            some FieldODEEventHandler stops it at some point.
        
        Raises:
            hipparchus: if integration step is too small
            hipparchus: if the location of an event cannot be bracketed
            hipparchus: if the number of functions evaluations is exceeded
        
        
        """
        ...
    def isUsingFieldCoefficients(self) -> bool:
        """
        Getter for the flag between real or Field coefficients in the Butcher array.
        
        Specified by: isUsingFieldCoefficients in interface FieldExplicitRungeKuttaIntegrator
        
        Returns:
            flag
        
        
        """
        ...
    def setUsingFieldCoefficients(self, usingFieldCoefficients: bool) -> None:
        """
        Setter for the flag between real or Field coefficients in the Butcher array.
        
        Parameters:
            usingFieldCoefficients (boolean): new value for flag
        
        
        """
        ...

class FixedStepRungeKuttaIntegrator(org.hipparchus.ode.AbstractIntegrator, ExplicitRungeKuttaIntegrator):
    """
    implements ExplicitRungeKuttaIntegrator
    
    This class implements the common part of all fixed step Runge-Kutta integrators for Ordinary Differential Equations.
    
    These methods are explicit Runge-Kutta methods, their Butcher arrays are as follows :
    
        0  | c2  | a21 c3  | a31  a32 ... |        ... cs  | as1  as2  ...  ass-1 |-------------------------- |  b1   b2  ...   bs-1  bs
    
          - EulerIntegrator
          - ClassicalRungeKuttaIntegrator
          - GillIntegrator
          - MidpointIntegrator
    """
    def getDefaultStep(self) -> float:
        """
        Getter for the default, positive step-size assigned at constructor level.
        
        Returns:
            step
        
        
        """
        ...
    @typing.overload
    def integrate(self, ordinaryDifferentialEquation: org.hipparchus.ode.OrdinaryDifferentialEquation, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...
    @typing.overload
    def integrate(self, expandableODE: org.hipparchus.ode.ExpandableODE, oDEState: org.hipparchus.ode.ODEState, double: float) -> org.hipparchus.ode.ODEStateAndDerivative: ...

_ClassicalRungeKuttaFieldIntegrator__T = typing.TypeVar('_ClassicalRungeKuttaFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class ClassicalRungeKuttaFieldIntegrator(FixedStepRungeKuttaFieldIntegrator[_ClassicalRungeKuttaFieldIntegrator__T], typing.Generic[_ClassicalRungeKuttaFieldIntegrator__T]):
    """
    This class implements the classical fourth order Runge-Kutta integrator for Ordinary Differential Equations (it is the most often used Runge-Kutta method).
    
    This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        0  |  0    0    0    0 1/2 | 1/2   0    0    0 1/2 |  0   1/2   0    0 1  |  0    0    1    0 |-------------------- | 1/6  1/3  1/3  1/6
    
          - EulerFieldIntegrator
          - GillFieldIntegrator
          - MidpointFieldIntegrator
          - ThreeEighthesFieldIntegrator
          - LutherFieldIntegrator
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    def __init__(self, field: org.hipparchus.Field[_ClassicalRungeKuttaFieldIntegrator__T], step: _ClassicalRungeKuttaFieldIntegrator__T):
        """
        Simple constructor. Build a fourth-order Runge-Kutta integrator with the given step.
        
        Parameters:
            field (hipparchus<ClassicalRungeKuttaFieldIntegrator> field): field to which the time and state vector elements belong
            step (ClassicalRungeKuttaFieldIntegrator): integration step
        
        
        """
        ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[_ClassicalRungeKuttaFieldIntegrator__T]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[_ClassicalRungeKuttaFieldIntegrator__T]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[_ClassicalRungeKuttaFieldIntegrator__T]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...

class ClassicalRungeKuttaIntegrator(FixedStepRungeKuttaIntegrator):
    """
    This class implements the classical fourth order Runge-Kutta integrator for Ordinary Differential Equations (it is the most often used Runge-Kutta method).
    
    This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        0  |  0    0    0    0 1/2 | 1/2   0    0    0 1/2 |  0   1/2   0    0 1  |  0    0    1    0 |-------------------- | 1/6  1/3  1/3  1/6
    
          - EulerIntegrator
          - GillIntegrator
          - MidpointIntegrator
          - ThreeEighthesIntegrator
          - LutherIntegrator
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    def __init__(self, step: float):
        """
        Simple constructor. Build a fourth-order Runge-Kutta integrator with the given step.
        
        Parameters:
            step (double): integration step
        
        
        """
        ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[float]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[float]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...

_DormandPrince54FieldIntegrator__T = typing.TypeVar('_DormandPrince54FieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class DormandPrince54FieldIntegrator(EmbeddedRungeKuttaFieldIntegrator[_DormandPrince54FieldIntegrator__T], typing.Generic[_DormandPrince54FieldIntegrator__T]):
    """
    This class implements the 5(4) Dormand-Prince integrator for Ordinary Differential Equations.
    
    This integrator is an embedded Runge-Kutta integrator of order 5(4) used in local extrapolation mode (i.e. the solution is computed using the high order formula) with stepsize control (and automatic step initialization) and continuous output. This method uses 7 functions evaluations per step. However, since this is an fsal, the last evaluation of one step is the same as the first evaluation of the next step and hence can be avoided. So the cost is really 6 functions evaluations per step.
    
    This method has been published (whithout the continuous output that was added by Shampine in 1986) in the following article :
    
      A family of embedded Runge-Kutta formulae J. R. Dormand and P. J. Prince Journal of Computational and Applied Mathematics volume 6, no 1, 1980, pp. 19-26
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_DormandPrince54FieldIntegrator__T], double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_DormandPrince54FieldIntegrator__T], double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[_DormandPrince54FieldIntegrator__T]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[_DormandPrince54FieldIntegrator__T]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[_DormandPrince54FieldIntegrator__T]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the order of the method.
        
        Specified by: getOrder in class EmbeddedRungeKuttaFieldIntegrator
        
        Returns:
            order of the method
        
        
        """
        ...

class DormandPrince54Integrator(EmbeddedRungeKuttaIntegrator):
    """
    This class implements the 5(4) Dormand-Prince integrator for Ordinary Differential Equations.
    
    This integrator is an embedded Runge-Kutta integrator of order 5(4) used in local extrapolation mode (i.e. the solution is computed using the high order formula) with stepsize control (and automatic step initialization) and continuous output. This method uses 7 functions evaluations per step. However, since this is an fsal, the last evaluation of one step is the same as the first evaluation of the next step and hence can be avoided. So the cost is really 6 functions evaluations per step.
    
    This method has been published (whithout the continuous output that was added by Shampine in 1986) in the following article :
    
      A family of embedded Runge-Kutta formulae J. R. Dormand and P. J. Prince Journal of Computational and Applied Mathematics volume 6, no 1, 1980, pp. 19-26
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[float]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[float]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the order of the method.
        
        Specified by: getOrder in class EmbeddedRungeKuttaIntegrator
        
        Returns:
            order of the method
        
        
        """
        ...

_DormandPrince853FieldIntegrator__T = typing.TypeVar('_DormandPrince853FieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class DormandPrince853FieldIntegrator(EmbeddedRungeKuttaFieldIntegrator[_DormandPrince853FieldIntegrator__T], typing.Generic[_DormandPrince853FieldIntegrator__T]):
    """
    This class implements the 8(5,3) Dormand-Prince integrator for Ordinary Differential Equations.
    
    This integrator is an embedded Runge-Kutta integrator of order 8(5,3) used in local extrapolation mode (i.e. the solution is computed using the high order formula) with stepsize control (and automatic step initialization) and continuous output. This method uses 12 functions evaluations per step for integration and 4 evaluations for interpolation. However, since the first interpolation evaluation is the same as the first integration evaluation of the next step, we have included it in the integrator rather than in the interpolator and specified the method was an fsal. Hence, despite we have 13 stages here, the cost is really 12 evaluations per step even if no interpolation is done, and the overcost of interpolation is only 3 evaluations.
    
    This method is based on an 8(6) method by Dormand and Prince (i.e. order 8 for the integration and order 6 for error estimation) modified by Hairer and Wanner to use a 5th order error estimator with 3rd order correction. This modification was introduced because the original method failed in some cases (wrong steps can be accepted when step size is too large, for example in the Brusselator problem) and also had severe difficulties when applied to problems with discontinuities. This modification is explained in the second edition of the first volume (Nonstiff Problems) of the reference book by Hairer, Norsett and Wanner: Solving Ordinary Differential Equations (Springer-Verlag, ISBN 3-540-56670-8).
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_DormandPrince853FieldIntegrator__T], double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_DormandPrince853FieldIntegrator__T], double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[_DormandPrince853FieldIntegrator__T]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[_DormandPrince853FieldIntegrator__T]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[_DormandPrince853FieldIntegrator__T]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the order of the method.
        
        Specified by: getOrder in class EmbeddedRungeKuttaFieldIntegrator
        
        Returns:
            order of the method
        
        
        """
        ...

class DormandPrince853Integrator(EmbeddedRungeKuttaIntegrator):
    """
    This class implements the 8(5,3) Dormand-Prince integrator for Ordinary Differential Equations.
    
    This integrator is an embedded Runge-Kutta integrator of order 8(5,3) used in local extrapolation mode (i.e. the solution is computed using the high order formula) with stepsize control (and automatic step initialization) and continuous output. This method uses 12 functions evaluations per step for integration and 4 evaluations for interpolation. However, since the first interpolation evaluation is the same as the first integration evaluation of the next step, we have included it in the integrator rather than in the interpolator and specified the method was an fsal. Hence, despite we have 13 stages here, the cost is really 12 evaluations per step even if no interpolation is done, and the overcost of interpolation is only 3 evaluations.
    
    This method is based on an 8(6) method by Dormand and Prince (i.e. order 8 for the integration and order 6 for error estimation) modified by Hairer and Wanner to use a 5th order error estimator with 3rd order correction. This modification was introduced because the original method failed in some cases (wrong steps can be accepted when step size is too large, for example in the Brusselator problem) and also had severe difficulties when applied to problems with discontinuities. This modification is explained in the second edition of the first volume (Nonstiff Problems) of the reference book by Hairer, Norsett and Wanner: Solving Ordinary Differential Equations (Springer-Verlag, ISBN 3-540-56670-8).
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[float]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[float]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the order of the method.
        
        Specified by: getOrder in class EmbeddedRungeKuttaIntegrator
        
        Returns:
            order of the method
        
        
        """
        ...

_EulerFieldIntegrator__T = typing.TypeVar('_EulerFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class EulerFieldIntegrator(FixedStepRungeKuttaFieldIntegrator[_EulerFieldIntegrator__T], typing.Generic[_EulerFieldIntegrator__T]):
    """
    This class implements a simple Euler integrator for Ordinary Differential Equations.
    
    The Euler algorithm is the simplest one that can be used to integrate ordinary differential equations. It is a simple inversion of the forward difference expression : f'=(f(t+h)-f(t))/h which leads to f(t+h)=f(t)+hf'. The interpolation scheme used for dense output is the linear scheme already used for integration.
    
    This algorithm looks cheap because it needs only one function evaluation per step. However, as it uses linear estimates, it needs very small steps to achieve high accuracy, and small steps lead to numerical errors and instabilities.
    
    This algorithm is almost never used and has been included in this package only as a comparison reference for more useful integrators.
    
          - MidpointFieldIntegrator
          - ClassicalRungeKuttaFieldIntegrator
          - GillFieldIntegrator
          - ThreeEighthesFieldIntegrator
          - LutherFieldIntegrator
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    def __init__(self, field: org.hipparchus.Field[_EulerFieldIntegrator__T], step: _EulerFieldIntegrator__T):
        """
        Simple constructor. Build an Euler integrator with the given step.
        
        Parameters:
            field (hipparchus<EulerFieldIntegrator> field): field to which the time and state vector elements belong
            step (EulerFieldIntegrator): integration step
        
        
        """
        ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[_EulerFieldIntegrator__T]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[_EulerFieldIntegrator__T]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[_EulerFieldIntegrator__T]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...

class EulerIntegrator(FixedStepRungeKuttaIntegrator):
    """
    This class implements a simple Euler integrator for Ordinary Differential Equations.
    
    The Euler algorithm is the simplest one that can be used to integrate ordinary differential equations. It is a simple inversion of the forward difference expression : f'=(f(t+h)-f(t))/h which leads to f(t+h)=f(t)+hf'. The interpolation scheme used for dense output is the linear scheme already used for integration.
    
    This algorithm looks cheap because it needs only one function evaluation per step. However, as it uses linear estimates, it needs very small steps to achieve high accuracy, and small steps lead to numerical errors and instabilities.
    
    This algorithm is almost never used and has been included in this package only as a comparison reference for more useful integrators.
    
          - MidpointIntegrator
          - ClassicalRungeKuttaIntegrator
          - GillIntegrator
          - ThreeEighthesIntegrator
          - LutherIntegrator
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    def __init__(self, step: float):
        """
        Simple constructor. Build an Euler integrator with the given step.
        
        Parameters:
            step (double): integration step
        
        
        """
        ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[float]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[float]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...

_GillFieldIntegrator__T = typing.TypeVar('_GillFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class GillFieldIntegrator(FixedStepRungeKuttaFieldIntegrator[_GillFieldIntegrator__T], typing.Generic[_GillFieldIntegrator__T]):
    """
    This class implements the Gill fourth order Runge-Kutta integrator for Ordinary Differential Equations .
    
    This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        0  |    0        0       0      0 1/2 |   1/2       0       0      0 1/2 | (q-1)/2  (2-q)/2    0      0 1  |    0       -q/2  (2+q)/2   0 |------------------------------- |   1/6    (2-q)/6 (2+q)/6  1/6
    
    where q = sqrt(2)
    
          - EulerFieldIntegrator
          - ClassicalRungeKuttaFieldIntegrator
          - MidpointFieldIntegrator
          - ThreeEighthesFieldIntegrator
          - LutherFieldIntegrator
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    def __init__(self, field: org.hipparchus.Field[_GillFieldIntegrator__T], step: _GillFieldIntegrator__T):
        """
        Simple constructor. Build a fourth-order Gill integrator with the given step.
        
        Parameters:
            field (hipparchus<GillFieldIntegrator> field): field to which the time and state vector elements belong
            step (GillFieldIntegrator): integration step
        
        
        """
        ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[_GillFieldIntegrator__T]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[_GillFieldIntegrator__T]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[_GillFieldIntegrator__T]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...

class GillIntegrator(FixedStepRungeKuttaIntegrator):
    """
    This class implements the Gill fourth order Runge-Kutta integrator for Ordinary Differential Equations .
    
    This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        0  |    0        0       0      0 1/2 |   1/2       0       0      0 1/2 | (q-1)/2  (2-q)/2    0      0 1  |    0       -q/2  (2+q)/2   0 |------------------------------- |   1/6    (2-q)/6 (2+q)/6  1/6
    
    where q = sqrt(2)
    
          - EulerIntegrator
          - ClassicalRungeKuttaIntegrator
          - MidpointIntegrator
          - ThreeEighthesIntegrator
          - LutherIntegrator
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    def __init__(self, step: float):
        """
        Simple constructor. Build a fourth-order Gill integrator with the given step.
        
        Parameters:
            step (double): integration step
        
        
        """
        ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[float]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[float]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...

_HighamHall54FieldIntegrator__T = typing.TypeVar('_HighamHall54FieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class HighamHall54FieldIntegrator(EmbeddedRungeKuttaFieldIntegrator[_HighamHall54FieldIntegrator__T], typing.Generic[_HighamHall54FieldIntegrator__T]):
    """
    This class implements the 5(4) Higham and Hall integrator for Ordinary Differential Equations.
    
    This integrator is an embedded Runge-Kutta integrator of order 5(4) used in local extrapolation mode (i.e. the solution is computed using the high order formula) with stepsize control (and automatic step initialization) and continuous output. This method uses 7 functions evaluations per step.
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_HighamHall54FieldIntegrator__T], double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_HighamHall54FieldIntegrator__T], double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[_HighamHall54FieldIntegrator__T]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[_HighamHall54FieldIntegrator__T]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[_HighamHall54FieldIntegrator__T]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the order of the method.
        
        Specified by: getOrder in class EmbeddedRungeKuttaFieldIntegrator
        
        Returns:
            order of the method
        
        
        """
        ...

class HighamHall54Integrator(EmbeddedRungeKuttaIntegrator):
    """
    This class implements the 5(4) Higham and Hall integrator for Ordinary Differential Equations.
    
    This integrator is an embedded Runge-Kutta integrator of order 5(4) used in local extrapolation mode (i.e. the solution is computed using the high order formula) with stepsize control (and automatic step initialization) and continuous output. This method uses 7 functions evaluations per step.
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[float]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[float]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the order of the method.
        
        Specified by: getOrder in class EmbeddedRungeKuttaIntegrator
        
        Returns:
            order of the method
        
        
        """
        ...

_LutherFieldIntegrator__T = typing.TypeVar('_LutherFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class LutherFieldIntegrator(FixedStepRungeKuttaFieldIntegrator[_LutherFieldIntegrator__T], typing.Generic[_LutherFieldIntegrator__T]):
    """
    This class implements the Luther sixth order Runge-Kutta integrator for Ordinary Differential Equations.
    
    This method is described in H. A. Luther 1968 paper ` An explicit Sixth-Order Runge-Kutta Formula <http://www.ams.org/journals/mcom/1968-22-102/S0025-5718-68-99876-1/S0025-5718-68-99876-1.pdf>`.
    
    This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
            0   |               0                     0                     0                     0                     0                     0 1   |               1                     0                     0                     0                     0                     0 1/2  |              3/8                   1/8                    0                     0                     0                     0 2/3  |              8/27                  2/27                  8/27                   0                     0                     0 (7-q)/14 | (  -21 +   9q)/392    (  -56 +   8q)/392    (  336 -  48q)/392    (  -63 +   3q)/392                  0                     0 (7+q)/14 | (-1155 - 255q)/1960   ( -280 -  40q)/1960   (    0 - 320q)/1960   (   63 + 363q)/1960   ( 2352 + 392q)/1960                 0 1   | (  330 + 105q)/180    (  120 +   0q)/180    ( -200 + 280q)/180    (  126 - 189q)/180    ( -686 - 126q)/180     ( 490 -  70q)/180 |-------------------------------------------------------------------------------------------------------------------------------------------------- |              1/20                   0                   16/45                  0                   49/180                 49/180         1/20
    
    where q = √21
    
          - EulerFieldIntegrator
          - ClassicalRungeKuttaFieldIntegrator
          - GillFieldIntegrator
          - MidpointFieldIntegrator
          - ThreeEighthesFieldIntegrator
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    def __init__(self, field: org.hipparchus.Field[_LutherFieldIntegrator__T], step: _LutherFieldIntegrator__T):
        """
        Simple constructor. Build a fourth-order Luther integrator with the given step.
        
        Parameters:
            field (hipparchus<LutherFieldIntegrator> field): field to which the time and state vector elements belong
            step (LutherFieldIntegrator): integration step
        
        
        """
        ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[_LutherFieldIntegrator__T]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[_LutherFieldIntegrator__T]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[_LutherFieldIntegrator__T]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...

class LutherIntegrator(FixedStepRungeKuttaIntegrator):
    """
    This class implements the Luther sixth order Runge-Kutta integrator for Ordinary Differential Equations.
    
    This method is described in H. A. Luther 1968 paper ` An explicit Sixth-Order Runge-Kutta Formula <http://www.ams.org/journals/mcom/1968-22-102/S0025-5718-68-99876-1/S0025-5718-68-99876-1.pdf>`.
    
    This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
            0   |               0                     0                     0                     0                     0                     0 1   |               1                     0                     0                     0                     0                     0 1/2  |              3/8                   1/8                    0                     0                     0                     0 2/3  |              8/27                  2/27                  8/27                   0                     0                     0 (7-q)/14 | (  -21 +   9q)/392    (  -56 +   8q)/392    (  336 -  48q)/392    (  -63 +   3q)/392                  0                     0 (7+q)/14 | (-1155 - 255q)/1960   ( -280 -  40q)/1960   (    0 - 320q)/1960   (   63 + 363q)/1960   ( 2352 + 392q)/1960                 0 1   | (  330 + 105q)/180    (  120 +   0q)/180    ( -200 + 280q)/180    (  126 - 189q)/180    ( -686 - 126q)/180     ( 490 -  70q)/180 |-------------------------------------------------------------------------------------------------------------------------------------------------- |              1/20                   0                   16/45                  0                   49/180                 49/180         1/20
    
    where q = √21
    
          - EulerIntegrator
          - ClassicalRungeKuttaIntegrator
          - GillIntegrator
          - MidpointIntegrator
          - ThreeEighthesIntegrator
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    def __init__(self, step: float):
        """
        Simple constructor. Build a fourth-order Luther integrator with the given step.
        
        Parameters:
            step (double): integration step
        
        
        """
        ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[float]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[float]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...

_MidpointFieldIntegrator__T = typing.TypeVar('_MidpointFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class MidpointFieldIntegrator(FixedStepRungeKuttaFieldIntegrator[_MidpointFieldIntegrator__T], typing.Generic[_MidpointFieldIntegrator__T]):
    """
    This class implements a second order Runge-Kutta integrator for Ordinary Differential Equations.
    
    This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        0  |  0    0 1/2 | 1/2   0 |---------- |  0    1
    
          - EulerFieldIntegrator
          - ClassicalRungeKuttaFieldIntegrator
          - GillFieldIntegrator
          - ThreeEighthesFieldIntegrator
          - LutherFieldIntegrator
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    def __init__(self, field: org.hipparchus.Field[_MidpointFieldIntegrator__T], step: _MidpointFieldIntegrator__T):
        """
        Simple constructor. Build a midpoint integrator with the given step.
        
        Parameters:
            field (hipparchus<MidpointFieldIntegrator> field): field to which the time and state vector elements belong
            step (MidpointFieldIntegrator): integration step
        
        
        """
        ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[_MidpointFieldIntegrator__T]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[_MidpointFieldIntegrator__T]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[_MidpointFieldIntegrator__T]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...

class MidpointIntegrator(FixedStepRungeKuttaIntegrator):
    """
    This class implements a second order Runge-Kutta integrator for Ordinary Differential Equations.
    
    This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        0  |  0    0 1/2 | 1/2   0 |---------- |  0    1
    
          - EulerIntegrator
          - ClassicalRungeKuttaIntegrator
          - GillIntegrator
          - ThreeEighthesIntegrator
          - LutherIntegrator
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    def __init__(self, step: float):
        """
        Simple constructor. Build a midpoint integrator with the given step.
        
        Parameters:
            step (double): integration step
        
        
        """
        ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[float]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[float]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...

_ThreeEighthesFieldIntegrator__T = typing.TypeVar('_ThreeEighthesFieldIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class ThreeEighthesFieldIntegrator(FixedStepRungeKuttaFieldIntegrator[_ThreeEighthesFieldIntegrator__T], typing.Generic[_ThreeEighthesFieldIntegrator__T]):
    """
    This class implements the 3/8 fourth order Runge-Kutta integrator for Ordinary Differential Equations.
    
    This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        0  |  0    0    0    0 1/3 | 1/3   0    0    0 2/3 |-1/3   1    0    0 1  |  1   -1    1    0 |-------------------- | 1/8  3/8  3/8  1/8
    
          - EulerFieldIntegrator
          - ClassicalRungeKuttaFieldIntegrator
          - GillFieldIntegrator
          - MidpointFieldIntegrator
          - LutherFieldIntegrator
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    def __init__(self, field: org.hipparchus.Field[_ThreeEighthesFieldIntegrator__T], step: _ThreeEighthesFieldIntegrator__T):
        """
        Simple constructor. Build a 3/8 integrator with the given step.
        
        Parameters:
            field (hipparchus<ThreeEighthesFieldIntegrator> field): field to which the time and state vector elements belong
            step (ThreeEighthesFieldIntegrator): integration step
        
        
        """
        ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[_ThreeEighthesFieldIntegrator__T]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[_ThreeEighthesFieldIntegrator__T]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[_ThreeEighthesFieldIntegrator__T]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...

class ThreeEighthesIntegrator(FixedStepRungeKuttaIntegrator):
    """
    This class implements the 3/8 fourth order Runge-Kutta integrator for Ordinary Differential Equations.
    
    This method is an explicit Runge-Kutta method, its Butcher-array is the following one :
    
        0  |  0    0    0    0 1/3 | 1/3   0    0    0 2/3 |-1/3   1    0    0 1  |  1   -1    1    0 |-------------------- | 1/8  3/8  3/8  1/8
    
          - EulerIntegrator
          - ClassicalRungeKuttaIntegrator
          - GillIntegrator
          - MidpointIntegrator
          - LutherIntegrator
    """
    METHOD_NAME: typing.ClassVar[str] = ...
    """
    Name of integration scheme.
    
          - constant
    
    
    
    """
    def __init__(self, step: float):
        """
        Simple constructor. Build a 3/8 integrator with the given step.
        
        Parameters:
            step (double): integration step
        
        
        """
        ...
    def getA(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the internal weights from Butcher array (without the first empty row).
        
        Returns:
            internal weights from Butcher array (without the first empty row)
        
        
        """
        ...
    def getB(self) -> typing.MutableSequence[float]:
        """
        Get the external weights for the high order method from Butcher array.
        
        Returns:
            external weights for the high order method from Butcher array
        
        
        """
        ...
    def getC(self) -> typing.MutableSequence[float]:
        """
        Get the time steps from Butcher array (without the first zero).
        
        Returns:
            time steps from Butcher array (without the first zero
        
        
        """
        ...


class __module_protocol__(Protocol):
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
    ExplicitRungeKuttaIntegrator: typing.Type[ExplicitRungeKuttaIntegrator]
    FieldButcherArrayProvider: typing.Type[FieldButcherArrayProvider]
    FieldExplicitRungeKuttaIntegrator: typing.Type[FieldExplicitRungeKuttaIntegrator]
    FixedStepRungeKuttaFieldIntegrator: typing.Type[FixedStepRungeKuttaFieldIntegrator]
    FixedStepRungeKuttaIntegrator: typing.Type[FixedStepRungeKuttaIntegrator]
    GillFieldIntegrator: typing.Type[GillFieldIntegrator]
    GillIntegrator: typing.Type[GillIntegrator]
    GraggBulirschStoerIntegrator: typing.Type[GraggBulirschStoerIntegrator]
    HighamHall54FieldIntegrator: typing.Type[HighamHall54FieldIntegrator]
    HighamHall54Integrator: typing.Type[HighamHall54Integrator]
    LutherFieldIntegrator: typing.Type[LutherFieldIntegrator]
    LutherIntegrator: typing.Type[LutherIntegrator]
    MidpointFieldIntegrator: typing.Type[MidpointFieldIntegrator]
    MidpointIntegrator: typing.Type[MidpointIntegrator]
    StepsizeHelper: typing.Type[StepsizeHelper]
    ThreeEighthesFieldIntegrator: typing.Type[ThreeEighthesFieldIntegrator]
    ThreeEighthesIntegrator: typing.Type[ThreeEighthesIntegrator]
    interpolators: org.hipparchus.ode.nonstiff.interpolators.__module_protocol__
