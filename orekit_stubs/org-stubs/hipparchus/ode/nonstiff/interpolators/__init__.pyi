
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.hipparchus
import org.hipparchus.linear
import org.hipparchus.ode
import org.hipparchus.ode.sampling
import typing



_AdamsFieldStateInterpolator__T = typing.TypeVar('_AdamsFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdamsFieldStateInterpolator(org.hipparchus.ode.sampling.AbstractFieldODEStateInterpolator[_AdamsFieldStateInterpolator__T], typing.Generic[_AdamsFieldStateInterpolator__T]):
    """
    This class implements an interpolator for Adams integrators using Nordsieck representation.
    
    This interpolator computes dense output around the current point. The interpolation equation is based on Taylor series formulas.
    
          - AdamsBashforthFieldIntegrator
          - AdamsMoultonFieldIntegrator
    """
    def __init__(self, stepSize: _AdamsFieldStateInterpolator__T, reference: org.hipparchus.ode.FieldODEStateAndDerivative[_AdamsFieldStateInterpolator__T], scaled: typing.Union[typing.List[_AdamsFieldStateInterpolator__T], jpype.JArray], nordsieck: org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsFieldStateInterpolator__T], isForward: bool, globalPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_AdamsFieldStateInterpolator__T], globalCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_AdamsFieldStateInterpolator__T], equationsMapper: org.hipparchus.ode.FieldEquationsMapper[_AdamsFieldStateInterpolator__T]):
        """
        Simple constructor.
        
        Parameters:
            stepSize (AdamsFieldStateInterpolator): step size used in the scaled and Nordsieck arrays
            reference (FieldODEStateAndDerivative<AdamsFieldStateInterpolator> reference): reference state from which Taylor expansion are estimated
            scaled (AdamsFieldStateInterpolator[]): first scaled derivative
            nordsieck (hipparchus<AdamsFieldStateInterpolator> nordsieck): Nordsieck vector
            isForward (boolean): integration direction indicator
            globalPreviousState (FieldODEStateAndDerivative<AdamsFieldStateInterpolator> globalPreviousState): start of the global step
            globalCurrentState (FieldODEStateAndDerivative<AdamsFieldStateInterpolator> globalCurrentState): end of the global step
            equationsMapper (FieldEquationsMapper<AdamsFieldStateInterpolator> equationsMapper): mapper for ODE equations primary and secondary components
        
        
        """
        ...
    def getNordsieck(self) -> org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsFieldStateInterpolator__T]:
        """
        Get the Nordsieck vector.
        
        Returns:
            Nordsieck vector
        
        
        """
        ...
    def getScaled(self) -> typing.MutableSequence[_AdamsFieldStateInterpolator__T]:
        """
        Get the first scaled derivative.
        
        Returns:
            first scaled derivative
        
        
        """
        ...
    _taylor__S = typing.TypeVar('_taylor__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    @staticmethod
    def taylor(equationsMapper: org.hipparchus.ode.FieldEquationsMapper[_taylor__S], reference: org.hipparchus.ode.FieldODEStateAndDerivative[_taylor__S], time: _taylor__S, stepSize: _taylor__S, scaled: typing.Union[typing.List[_taylor__S], jpype.JArray], nordsieck: org.hipparchus.linear.Array2DRowFieldMatrix[_taylor__S]) -> org.hipparchus.ode.FieldODEStateAndDerivative[_taylor__S]:
        """
        Estimate state by applying Taylor formula.
        
        Parameters:
            equationsMapper (FieldEquationsMapper<S> equationsMapper): mapper for ODE equations primary and secondary components
            reference (FieldODEStateAndDerivative<S> reference): reference state
            time (S): time at which state must be estimated
            stepSize (S): step size used in the scaled and Nordsieck arrays
            scaled (S[]): first scaled derivative
            nordsieck (hipparchus<S> nordsieck): Nordsieck vector
        
        Returns:
            estimated state
        
        
        """
        ...

class AdamsStateInterpolator(org.hipparchus.ode.sampling.AbstractODEStateInterpolator):
    """
    This class implements an interpolator for integrators using Nordsieck representation.
    
    This interpolator computes dense output around the current point. The interpolation equation is based on Taylor series formulas.
    
          - AdamsBashforthIntegrator
          - AdamsMoultonIntegrator
          - serialized
    """
    def __init__(self, stepSize: float, reference: org.hipparchus.ode.ODEStateAndDerivative, scaled: typing.Union[typing.List[float], jpype.JArray], nordsieck: org.hipparchus.linear.Array2DRowRealMatrix, isForward: bool, globalPreviousState: org.hipparchus.ode.ODEStateAndDerivative, globalCurrentState: org.hipparchus.ode.ODEStateAndDerivative, equationsMapper: org.hipparchus.ode.EquationsMapper):
        """
        Simple constructor.
        
        Parameters:
            stepSize (double): step size used in the scaled and Nordsieck arrays
            reference (ODEStateAndDerivative): reference state from which Taylor expansion are estimated
            scaled (double[]): first scaled derivative
            nordsieck (hipparchus): Nordsieck vector
            isForward (boolean): integration direction indicator
            globalPreviousState (ODEStateAndDerivative): start of the global step
            globalCurrentState (ODEStateAndDerivative): end of the global step
            equationsMapper (EquationsMapper): mapper for ODE equations primary and secondary components
        
        
        """
        ...
    def getNordsieck(self) -> org.hipparchus.linear.Array2DRowRealMatrix:
        """
        Get the Nordsieck vector.
        
        Returns:
            Nordsieck vector
        
        
        """
        ...
    def getScaled(self) -> typing.MutableSequence[float]:
        """
        Get the first scaled derivative.
        
        Returns:
            first scaled derivative
        
        
        """
        ...
    @staticmethod
    def taylor(equationsMapper: org.hipparchus.ode.EquationsMapper, reference: org.hipparchus.ode.ODEStateAndDerivative, time: float, stepSize: float, scaled: typing.Union[typing.List[float], jpype.JArray], nordsieck: org.hipparchus.linear.Array2DRowRealMatrix) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
        Estimate state by applying Taylor formula.
        
        Parameters:
            equationsMapper (EquationsMapper): mapper for ODE equations primary and secondary components
            reference (ODEStateAndDerivative): reference state
            time (double): time at which state must be estimated
            stepSize (double): step size used in the scaled and Nordsieck arrays
            scaled (double[]): first scaled derivative
            nordsieck (hipparchus): Nordsieck vector
        
        Returns:
            estimated state
        
        
        """
        ...

class GraggBulirschStoerStateInterpolator(org.hipparchus.ode.sampling.AbstractODEStateInterpolator):
    """
    This class implements an interpolator for the Gragg-Bulirsch-Stoer integrator.
    
    This interpolator compute dense output inside the last step produced by a Gragg-Bulirsch-Stoer integrator.
    
    This implementation is basically a reimplementation in Java of the `odex <http://www.unige.ch/math/folks/hairer/prog/nonstiff/odex.f>` fortran code by E. Hairer and G. Wanner. The redistribution policy for this code is available `here <http://www.unige.ch/~hairer/prog/licence.txt>`, for convenience, it is reproduced below.
    
        Copyright (c) 2004, Ernst Hairer
    
        Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
    
          - Redistributions of source code must retain the above copyright notice, this list of conditions and the following
            disclaimer.
          - Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
            disclaimer in the documentation and/or other materials provided with the distribution.
    
        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    
          - GraggBulirschStoerIntegrator
          - serialized
    """
    def __init__(self, forward: bool, globalPreviousState: org.hipparchus.ode.ODEStateAndDerivative, globalCurrentState: org.hipparchus.ode.ODEStateAndDerivative, softPreviousState: org.hipparchus.ode.ODEStateAndDerivative, softCurrentState: org.hipparchus.ode.ODEStateAndDerivative, mapper: org.hipparchus.ode.EquationsMapper, yMidDots: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], mu: int):
        """
        Simple constructor.
        
        Parameters:
            forward (boolean): integration direction indicator
            globalPreviousState (ODEStateAndDerivative): start of the global step
            globalCurrentState (ODEStateAndDerivative): end of the global step
            softPreviousState (ODEStateAndDerivative): start of the restricted step
            softCurrentState (ODEStateAndDerivative): end of the restricted step
            mapper (EquationsMapper): equations mapper for the all equations
            yMidDots (double[][]): scaled derivatives at the middle of the step $\tau$ (element k is $h^{k} d^{k}y(\tau)/dt^{k}$ where h is step size...)
            mu (int): degree of the interpolation polynomial
        
        
        """
        ...
    def estimateError(self, scale: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Estimate interpolation error.
        
        Parameters:
            scale (double[]): scaling array
        
        Returns:
            estimate of the interpolation error
        
        
        """
        ...

_RungeKuttaFieldStateInterpolator__T = typing.TypeVar('_RungeKuttaFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class RungeKuttaFieldStateInterpolator(org.hipparchus.ode.sampling.AbstractFieldODEStateInterpolator[_RungeKuttaFieldStateInterpolator__T], typing.Generic[_RungeKuttaFieldStateInterpolator__T]):
    """
    This class represents an interpolator over the last step during an ODE integration for Runge-Kutta and embedded Runge-Kutta integrators.
    
          - FixedStepRungeKuttaFieldIntegrator
          - EmbeddedRungeKuttaFieldIntegrator
    """
    ...

class RungeKuttaStateInterpolator(org.hipparchus.ode.sampling.AbstractODEStateInterpolator):
    """
    This class represents an interpolator over the last step during an ODE integration for Runge-Kutta and embedded Runge-Kutta integrators.
    
          - FixedStepRungeKuttaIntegrator
          - EmbeddedRungeKuttaIntegrator
          - serialized
    """
    ...

_ClassicalRungeKuttaFieldStateInterpolator__T = typing.TypeVar('_ClassicalRungeKuttaFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class ClassicalRungeKuttaFieldStateInterpolator(RungeKuttaFieldStateInterpolator[_ClassicalRungeKuttaFieldStateInterpolator__T], typing.Generic[_ClassicalRungeKuttaFieldStateInterpolator__T]):
    """
    This class implements a step interpolator for the classical fourth order Runge-Kutta integrator.
    
    This interpolator allows to compute dense output inside the last step computed. The interpolation equation is consistent with the integration scheme :
    
      - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ (h/6) [ (6 - 9 θ + 4 θ :sup:`2` ) y' :sub:`1` + ( 6 θ - 4 θ :sup:`2` )
        (y' :sub:`2` + y' :sub:`3` ) + ( -3 θ + 4 θ :sup:`2` ) y' :sub:`4` ]
      - Using reference point at step end:
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) + (1 - θ) (h/6) [ (-4 θ^2 + 5 θ - 1) y' :sub:`1` +(4 θ^2 - 2 θ - 2) (y' :sub:`2` + y' :sub:`3` ) -(4 θ^2 + θ + 1) y' :sub:`4` ]
    
    where θ belongs to [0 ; 1] and where y' :sub:`1` to y' :sub:`4` are the four evaluations of the derivatives already computed during the step.
    
          - ClassicalRungeKuttaFieldIntegrator
    """
    def __init__(self, field: org.hipparchus.Field[_ClassicalRungeKuttaFieldStateInterpolator__T], forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[_ClassicalRungeKuttaFieldStateInterpolator__T]], jpype.JArray], globalPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_ClassicalRungeKuttaFieldStateInterpolator__T], globalCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_ClassicalRungeKuttaFieldStateInterpolator__T], softPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_ClassicalRungeKuttaFieldStateInterpolator__T], softCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_ClassicalRungeKuttaFieldStateInterpolator__T], mapper: org.hipparchus.ode.FieldEquationsMapper[_ClassicalRungeKuttaFieldStateInterpolator__T]):
        """
        Simple constructor.
        
        Parameters:
            field (hipparchus<ClassicalRungeKuttaFieldStateInterpolator> field): field to which the time and state vector elements belong
            forward (boolean): integration direction indicator
            yDotK (ClassicalRungeKuttaFieldStateInterpolator[][]): slopes at the intermediate points
            globalPreviousState (FieldODEStateAndDerivative<ClassicalRungeKuttaFieldStateInterpolator> globalPreviousState): start of the global step
            globalCurrentState (FieldODEStateAndDerivative<ClassicalRungeKuttaFieldStateInterpolator> globalCurrentState): end of the global step
            softPreviousState (FieldODEStateAndDerivative<ClassicalRungeKuttaFieldStateInterpolator> softPreviousState): start of the restricted step
            softCurrentState (FieldODEStateAndDerivative<ClassicalRungeKuttaFieldStateInterpolator> softCurrentState): end of the restricted step
            mapper (FieldEquationsMapper<ClassicalRungeKuttaFieldStateInterpolator> mapper): equations mapper for the all equations
        
        
        """
        ...

class ClassicalRungeKuttaStateInterpolator(RungeKuttaStateInterpolator):
    """
    This class implements a step interpolator for the classical fourth order Runge-Kutta integrator.
    
    This interpolator allows to compute dense output inside the last step computed. The interpolation equation is consistent with the integration scheme :
    
      - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ (h/6) [ (6 - 9 θ + 4 θ :sup:`2` ) y' :sub:`1` + ( 6 θ - 4 θ :sup:`2` )
        (y' :sub:`2` + y' :sub:`3` ) + ( -3 θ + 4 θ :sup:`2` ) y' :sub:`4` ]
      - Using reference point at step end:
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) + (1 - θ) (h/6) [ (-4 θ^2 + 5 θ - 1) y' :sub:`1` +(4 θ^2 - 2 θ - 2) (y' :sub:`2` + y' :sub:`3` ) -(4 θ^2 + θ + 1) y' :sub:`4` ]
    
    where θ belongs to [0 ; 1] and where y' :sub:`1` to y' :sub:`4` are the four evaluations of the derivatives already computed during the step.
    
          - ClassicalRungeKuttaIntegrator
          - serialized
    """
    def __init__(self, forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], globalPreviousState: org.hipparchus.ode.ODEStateAndDerivative, globalCurrentState: org.hipparchus.ode.ODEStateAndDerivative, softPreviousState: org.hipparchus.ode.ODEStateAndDerivative, softCurrentState: org.hipparchus.ode.ODEStateAndDerivative, mapper: org.hipparchus.ode.EquationsMapper):
        """
        Simple constructor.
        
        Parameters:
            forward (boolean): integration direction indicator
            yDotK (double[][]): slopes at the intermediate points
            globalPreviousState (ODEStateAndDerivative): start of the global step
            globalCurrentState (ODEStateAndDerivative): end of the global step
            softPreviousState (ODEStateAndDerivative): start of the restricted step
            softCurrentState (ODEStateAndDerivative): end of the restricted step
            mapper (EquationsMapper): equations mapper for the all equations
        
        
        """
        ...

_DormandPrince54FieldStateInterpolator__T = typing.TypeVar('_DormandPrince54FieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class DormandPrince54FieldStateInterpolator(RungeKuttaFieldStateInterpolator[_DormandPrince54FieldStateInterpolator__T], typing.Generic[_DormandPrince54FieldStateInterpolator__T]):
    """
    This class represents an interpolator over the last step during an ODE integration for the 5(4) Dormand-Prince integrator.
    
          - DormandPrince54Integrator
    """
    def __init__(self, field: org.hipparchus.Field[_DormandPrince54FieldStateInterpolator__T], forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[_DormandPrince54FieldStateInterpolator__T]], jpype.JArray], globalPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince54FieldStateInterpolator__T], globalCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince54FieldStateInterpolator__T], softPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince54FieldStateInterpolator__T], softCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince54FieldStateInterpolator__T], mapper: org.hipparchus.ode.FieldEquationsMapper[_DormandPrince54FieldStateInterpolator__T]):
        """
        Simple constructor.
        
        Parameters:
            field (hipparchus<DormandPrince54FieldStateInterpolator> field): field to which the time and state vector elements belong
            forward (boolean): integration direction indicator
            yDotK (DormandPrince54FieldStateInterpolator[][]): slopes at the intermediate points
            globalPreviousState (FieldODEStateAndDerivative<DormandPrince54FieldStateInterpolator> globalPreviousState): start of the global step
            globalCurrentState (FieldODEStateAndDerivative<DormandPrince54FieldStateInterpolator> globalCurrentState): end of the global step
            softPreviousState (FieldODEStateAndDerivative<DormandPrince54FieldStateInterpolator> softPreviousState): start of the restricted step
            softCurrentState (FieldODEStateAndDerivative<DormandPrince54FieldStateInterpolator> softCurrentState): end of the restricted step
            mapper (FieldEquationsMapper<DormandPrince54FieldStateInterpolator> mapper): equations mapper for the all equations
        
        
        """
        ...

class DormandPrince54StateInterpolator(RungeKuttaStateInterpolator):
    """
    This class represents an interpolator over the last step during an ODE integration for the 5(4) Dormand-Prince integrator.
    
          - DormandPrince54Integrator
          - serialized
    """
    def __init__(self, forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], globalPreviousState: org.hipparchus.ode.ODEStateAndDerivative, globalCurrentState: org.hipparchus.ode.ODEStateAndDerivative, softPreviousState: org.hipparchus.ode.ODEStateAndDerivative, softCurrentState: org.hipparchus.ode.ODEStateAndDerivative, mapper: org.hipparchus.ode.EquationsMapper):
        """
        Simple constructor.
        
        Parameters:
            forward (boolean): integration direction indicator
            yDotK (double[][]): slopes at the intermediate points
            globalPreviousState (ODEStateAndDerivative): start of the global step
            globalCurrentState (ODEStateAndDerivative): end of the global step
            softPreviousState (ODEStateAndDerivative): start of the restricted step
            softCurrentState (ODEStateAndDerivative): end of the restricted step
            mapper (EquationsMapper): equations mapper for the all equations
        
        
        """
        ...

_DormandPrince853FieldStateInterpolator__T = typing.TypeVar('_DormandPrince853FieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class DormandPrince853FieldStateInterpolator(RungeKuttaFieldStateInterpolator[_DormandPrince853FieldStateInterpolator__T], typing.Generic[_DormandPrince853FieldStateInterpolator__T]):
    """
    This class represents an interpolator over the last step during an ODE integration for the 8(5,3) Dormand-Prince integrator.
    
          - DormandPrince853FieldIntegrator
    """
    def __init__(self, field: org.hipparchus.Field[_DormandPrince853FieldStateInterpolator__T], forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[_DormandPrince853FieldStateInterpolator__T]], jpype.JArray], globalPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince853FieldStateInterpolator__T], globalCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince853FieldStateInterpolator__T], softPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince853FieldStateInterpolator__T], softCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince853FieldStateInterpolator__T], mapper: org.hipparchus.ode.FieldEquationsMapper[_DormandPrince853FieldStateInterpolator__T]):
        """
        Simple constructor.
        
        Parameters:
            field (hipparchus<DormandPrince853FieldStateInterpolator> field): field to which the time and state vector elements belong
            forward (boolean): integration direction indicator
            yDotK (DormandPrince853FieldStateInterpolator[][]): slopes at the intermediate points
            globalPreviousState (FieldODEStateAndDerivative<DormandPrince853FieldStateInterpolator> globalPreviousState): start of the global step
            globalCurrentState (FieldODEStateAndDerivative<DormandPrince853FieldStateInterpolator> globalCurrentState): end of the global step
            softPreviousState (FieldODEStateAndDerivative<DormandPrince853FieldStateInterpolator> softPreviousState): start of the restricted step
            softCurrentState (FieldODEStateAndDerivative<DormandPrince853FieldStateInterpolator> softCurrentState): end of the restricted step
            mapper (FieldEquationsMapper<DormandPrince853FieldStateInterpolator> mapper): equations mapper for the all equations
        
        
        """
        ...

class DormandPrince853StateInterpolator(RungeKuttaStateInterpolator):
    """
    This class represents an interpolator over the last step during an ODE integration for the 8(5,3) Dormand-Prince integrator.
    
          - DormandPrince853Integrator
          - serialized
    """
    def __init__(self, forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], globalPreviousState: org.hipparchus.ode.ODEStateAndDerivative, globalCurrentState: org.hipparchus.ode.ODEStateAndDerivative, softPreviousState: org.hipparchus.ode.ODEStateAndDerivative, softCurrentState: org.hipparchus.ode.ODEStateAndDerivative, mapper: org.hipparchus.ode.EquationsMapper):
        """
        Simple constructor.
        
        Parameters:
            forward (boolean): integration direction indicator
            yDotK (double[][]): slopes at the intermediate points
            globalPreviousState (ODEStateAndDerivative): start of the global step
            globalCurrentState (ODEStateAndDerivative): end of the global step
            softPreviousState (ODEStateAndDerivative): start of the restricted step
            softCurrentState (ODEStateAndDerivative): end of the restricted step
            mapper (EquationsMapper): equations mapper for the all equations
        
        
        """
        ...

_EulerFieldStateInterpolator__T = typing.TypeVar('_EulerFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class EulerFieldStateInterpolator(RungeKuttaFieldStateInterpolator[_EulerFieldStateInterpolator__T], typing.Generic[_EulerFieldStateInterpolator__T]):
    """
    This class implements a linear interpolator for step.
    
    This interpolator computes dense output inside the last step computed. The interpolation equation is consistent with the integration scheme :
    
      - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ h y'
      - Using reference point at step end:
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) - (1-θ) h y'
    
    where θ belongs to [0 ; 1] and where y' is the evaluation of the derivatives already computed during the step.
    
          - EulerFieldIntegrator
    """
    def __init__(self, field: org.hipparchus.Field[_EulerFieldStateInterpolator__T], forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[_EulerFieldStateInterpolator__T]], jpype.JArray], globalPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_EulerFieldStateInterpolator__T], globalCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_EulerFieldStateInterpolator__T], softPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_EulerFieldStateInterpolator__T], softCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_EulerFieldStateInterpolator__T], mapper: org.hipparchus.ode.FieldEquationsMapper[_EulerFieldStateInterpolator__T]):
        """
        Simple constructor.
        
        Parameters:
            field (hipparchus<EulerFieldStateInterpolator> field): field to which the time and state vector elements belong
            forward (boolean): integration direction indicator
            yDotK (EulerFieldStateInterpolator[][]): slopes at the intermediate points
            globalPreviousState (FieldODEStateAndDerivative<EulerFieldStateInterpolator> globalPreviousState): start of the global step
            globalCurrentState (FieldODEStateAndDerivative<EulerFieldStateInterpolator> globalCurrentState): end of the global step
            softPreviousState (FieldODEStateAndDerivative<EulerFieldStateInterpolator> softPreviousState): start of the restricted step
            softCurrentState (FieldODEStateAndDerivative<EulerFieldStateInterpolator> softCurrentState): end of the restricted step
            mapper (FieldEquationsMapper<EulerFieldStateInterpolator> mapper): equations mapper for the all equations
        
        
        """
        ...

class EulerStateInterpolator(RungeKuttaStateInterpolator):
    """
    This class implements a linear interpolator for step.
    
    This interpolator computes dense output inside the last step computed. The interpolation equation is consistent with the integration scheme :
    
      - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ h y'
      - Using reference point at step end:
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) - (1-θ) h y'
    
    where θ belongs to [0 ; 1] and where y' is the evaluation of the derivatives already computed during the step.
    
          - EulerIntegrator
          - serialized
    """
    def __init__(self, forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], globalPreviousState: org.hipparchus.ode.ODEStateAndDerivative, globalCurrentState: org.hipparchus.ode.ODEStateAndDerivative, softPreviousState: org.hipparchus.ode.ODEStateAndDerivative, softCurrentState: org.hipparchus.ode.ODEStateAndDerivative, mapper: org.hipparchus.ode.EquationsMapper):
        """
        Simple constructor.
        
        Parameters:
            forward (boolean): integration direction indicator
            yDotK (double[][]): slopes at the intermediate points
            globalPreviousState (ODEStateAndDerivative): start of the global step
            globalCurrentState (ODEStateAndDerivative): end of the global step
            softPreviousState (ODEStateAndDerivative): start of the restricted step
            softCurrentState (ODEStateAndDerivative): end of the restricted step
            mapper (EquationsMapper): equations mapper for the all equations
        
        
        """
        ...

_GillFieldStateInterpolator__T = typing.TypeVar('_GillFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class GillFieldStateInterpolator(RungeKuttaFieldStateInterpolator[_GillFieldStateInterpolator__T], typing.Generic[_GillFieldStateInterpolator__T]):
    """
    This class implements a step interpolator for the Gill fourth order Runge-Kutta integrator.
    
    This interpolator allows to compute dense output inside the last step computed. The interpolation equation is consistent with the integration scheme :
    
      - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ (h/6) [ (6 - 9 θ + 4 θ :sup:`2` ) y' :sub:`1` + ( 6 θ - 4 θ :sup:`2` )
        ((1-1/√2) y' :sub:`2` + (1+1/√2)) y' :sub:`3` ) + ( - 3 θ + 4 θ :sup:`2` ) y' :sub:`4` ]
      - Using reference point at step start:
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) - (1 - θ) (h/6) [ (1 - 5 θ + 4 θ :sup:`2` ) y' :sub:`1` + (2 + 2 θ - 4 θ :sup:`2` ) ((1-1/√2) y' :sub:`2` + (1+1/√2)) y' :sub:`3` ) + (1 + θ + 4 θ :sup:`2` ) y' :sub:`4` ]
    
    where θ belongs to [0 ; 1] and where y' :sub:`1` to y' :sub:`4` are the four evaluations of the derivatives already computed during the step.
    
          - GillFieldIntegrator
    """
    def __init__(self, field: org.hipparchus.Field[_GillFieldStateInterpolator__T], forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[_GillFieldStateInterpolator__T]], jpype.JArray], globalPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_GillFieldStateInterpolator__T], globalCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_GillFieldStateInterpolator__T], softPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_GillFieldStateInterpolator__T], softCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_GillFieldStateInterpolator__T], mapper: org.hipparchus.ode.FieldEquationsMapper[_GillFieldStateInterpolator__T]):
        """
        Simple constructor.
        
        Parameters:
            field (hipparchus<GillFieldStateInterpolator> field): field to which the time and state vector elements belong
            forward (boolean): integration direction indicator
            yDotK (GillFieldStateInterpolator[][]): slopes at the intermediate points
            globalPreviousState (FieldODEStateAndDerivative<GillFieldStateInterpolator> globalPreviousState): start of the global step
            globalCurrentState (FieldODEStateAndDerivative<GillFieldStateInterpolator> globalCurrentState): end of the global step
            softPreviousState (FieldODEStateAndDerivative<GillFieldStateInterpolator> softPreviousState): start of the restricted step
            softCurrentState (FieldODEStateAndDerivative<GillFieldStateInterpolator> softCurrentState): end of the restricted step
            mapper (FieldEquationsMapper<GillFieldStateInterpolator> mapper): equations mapper for the all equations
        
        
        """
        ...

class GillStateInterpolator(RungeKuttaStateInterpolator):
    """
    This class implements a step interpolator for the Gill fourth order Runge-Kutta integrator.
    
    This interpolator allows to compute dense output inside the last step computed. The interpolation equation is consistent with the integration scheme :
    
      - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ (h/6) [ (6 - 9 θ + 4 θ :sup:`2` ) y' :sub:`1` + ( 6 θ - 4 θ :sup:`2` )
        ((1-1/√2) y' :sub:`2` + (1+1/√2)) y' :sub:`3` ) + ( - 3 θ + 4 θ :sup:`2` ) y' :sub:`4` ]
      - Using reference point at step start:
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) - (1 - θ) (h/6) [ (1 - 5 θ + 4 θ :sup:`2` ) y' :sub:`1` + (2 + 2 θ - 4 θ :sup:`2` ) ((1-1/√2) y' :sub:`2` + (1+1/√2)) y' :sub:`3` ) + (1 + θ + 4 θ :sup:`2` ) y' :sub:`4` ]
    
    where θ belongs to [0 ; 1] and where y' :sub:`1` to y' :sub:`4` are the four evaluations of the derivatives already computed during the step.
    
          - GillIntegrator
          - serialized
    """
    def __init__(self, forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], globalPreviousState: org.hipparchus.ode.ODEStateAndDerivative, globalCurrentState: org.hipparchus.ode.ODEStateAndDerivative, softPreviousState: org.hipparchus.ode.ODEStateAndDerivative, softCurrentState: org.hipparchus.ode.ODEStateAndDerivative, mapper: org.hipparchus.ode.EquationsMapper):
        """
        Simple constructor.
        
        Parameters:
            forward (boolean): integration direction indicator
            yDotK (double[][]): slopes at the intermediate points
            globalPreviousState (ODEStateAndDerivative): start of the global step
            globalCurrentState (ODEStateAndDerivative): end of the global step
            softPreviousState (ODEStateAndDerivative): start of the restricted step
            softCurrentState (ODEStateAndDerivative): end of the restricted step
            mapper (EquationsMapper): equations mapper for the all equations
        
        
        """
        ...

_HighamHall54FieldStateInterpolator__T = typing.TypeVar('_HighamHall54FieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class HighamHall54FieldStateInterpolator(RungeKuttaFieldStateInterpolator[_HighamHall54FieldStateInterpolator__T], typing.Generic[_HighamHall54FieldStateInterpolator__T]):
    """
    This class represents an interpolator over the last step during an ODE integration for the 5(4) Higham and Hall integrator.
    
          - HighamHall54FieldIntegrator
    """
    def __init__(self, field: org.hipparchus.Field[_HighamHall54FieldStateInterpolator__T], forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[_HighamHall54FieldStateInterpolator__T]], jpype.JArray], globalPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_HighamHall54FieldStateInterpolator__T], globalCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_HighamHall54FieldStateInterpolator__T], softPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_HighamHall54FieldStateInterpolator__T], softCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_HighamHall54FieldStateInterpolator__T], mapper: org.hipparchus.ode.FieldEquationsMapper[_HighamHall54FieldStateInterpolator__T]):
        """
        Simple constructor.
        
        Parameters:
            field (hipparchus<HighamHall54FieldStateInterpolator> field): field to which the time and state vector elements belong
            forward (boolean): integration direction indicator
            yDotK (HighamHall54FieldStateInterpolator[][]): slopes at the intermediate points
            globalPreviousState (FieldODEStateAndDerivative<HighamHall54FieldStateInterpolator> globalPreviousState): start of the global step
            globalCurrentState (FieldODEStateAndDerivative<HighamHall54FieldStateInterpolator> globalCurrentState): end of the global step
            softPreviousState (FieldODEStateAndDerivative<HighamHall54FieldStateInterpolator> softPreviousState): start of the restricted step
            softCurrentState (FieldODEStateAndDerivative<HighamHall54FieldStateInterpolator> softCurrentState): end of the restricted step
            mapper (FieldEquationsMapper<HighamHall54FieldStateInterpolator> mapper): equations mapper for the all equations
        
        
        """
        ...

class HighamHall54StateInterpolator(RungeKuttaStateInterpolator):
    """
    This class represents an interpolator over the last step during an ODE integration for the 5(4) Higham and Hall integrator.
    
          - HighamHall54Integrator
          - serialized
    """
    def __init__(self, forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], globalPreviousState: org.hipparchus.ode.ODEStateAndDerivative, globalCurrentState: org.hipparchus.ode.ODEStateAndDerivative, softPreviousState: org.hipparchus.ode.ODEStateAndDerivative, softCurrentState: org.hipparchus.ode.ODEStateAndDerivative, mapper: org.hipparchus.ode.EquationsMapper):
        """
        Simple constructor.
        
        Parameters:
            forward (boolean): integration direction indicator
            yDotK (double[][]): slopes at the intermediate points
            globalPreviousState (ODEStateAndDerivative): start of the global step
            globalCurrentState (ODEStateAndDerivative): end of the global step
            softPreviousState (ODEStateAndDerivative): start of the restricted step
            softCurrentState (ODEStateAndDerivative): end of the restricted step
            mapper (EquationsMapper): equations mapper for the all equations
        
        
        """
        ...

_LutherFieldStateInterpolator__T = typing.TypeVar('_LutherFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class LutherFieldStateInterpolator(RungeKuttaFieldStateInterpolator[_LutherFieldStateInterpolator__T], typing.Generic[_LutherFieldStateInterpolator__T]):
    """
    This class represents an interpolator over the last step during an ODE integration for the 6th order Luther integrator.
    
    This interpolator computes dense output inside the last step computed. The interpolation equation is consistent with the integration scheme.
    
          - LutherFieldIntegrator
    """
    def __init__(self, field: org.hipparchus.Field[_LutherFieldStateInterpolator__T], forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[_LutherFieldStateInterpolator__T]], jpype.JArray], globalPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_LutherFieldStateInterpolator__T], globalCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_LutherFieldStateInterpolator__T], softPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_LutherFieldStateInterpolator__T], softCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_LutherFieldStateInterpolator__T], mapper: org.hipparchus.ode.FieldEquationsMapper[_LutherFieldStateInterpolator__T]):
        """
        Simple constructor.
        
        Parameters:
            field (hipparchus<LutherFieldStateInterpolator> field): field to which the time and state vector elements belong
            forward (boolean): integration direction indicator
            yDotK (LutherFieldStateInterpolator[][]): slopes at the intermediate points
            globalPreviousState (FieldODEStateAndDerivative<LutherFieldStateInterpolator> globalPreviousState): start of the global step
            globalCurrentState (FieldODEStateAndDerivative<LutherFieldStateInterpolator> globalCurrentState): end of the global step
            softPreviousState (FieldODEStateAndDerivative<LutherFieldStateInterpolator> softPreviousState): start of the restricted step
            softCurrentState (FieldODEStateAndDerivative<LutherFieldStateInterpolator> softCurrentState): end of the restricted step
            mapper (FieldEquationsMapper<LutherFieldStateInterpolator> mapper): equations mapper for the all equations
        
        
        """
        ...

class LutherStateInterpolator(RungeKuttaStateInterpolator):
    """
    This class represents an interpolator over the last step during an ODE integration for the 6th order Luther integrator.
    
    This interpolator computes dense output inside the last step computed. The interpolation equation is consistent with the integration scheme.
    
          - LutherIntegrator
          - serialized
    """
    def __init__(self, forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], globalPreviousState: org.hipparchus.ode.ODEStateAndDerivative, globalCurrentState: org.hipparchus.ode.ODEStateAndDerivative, softPreviousState: org.hipparchus.ode.ODEStateAndDerivative, softCurrentState: org.hipparchus.ode.ODEStateAndDerivative, mapper: org.hipparchus.ode.EquationsMapper):
        """
        Simple constructor.
        
        Parameters:
            forward (boolean): integration direction indicator
            yDotK (double[][]): slopes at the intermediate points
            globalPreviousState (ODEStateAndDerivative): start of the global step
            globalCurrentState (ODEStateAndDerivative): end of the global step
            softPreviousState (ODEStateAndDerivative): start of the restricted step
            softCurrentState (ODEStateAndDerivative): end of the restricted step
            mapper (EquationsMapper): equations mapper for the all equations
        
        
        """
        ...

_MidpointFieldStateInterpolator__T = typing.TypeVar('_MidpointFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class MidpointFieldStateInterpolator(RungeKuttaFieldStateInterpolator[_MidpointFieldStateInterpolator__T], typing.Generic[_MidpointFieldStateInterpolator__T]):
    """
    This class implements a step interpolator for second order Runge-Kutta integrator.
    
    This interpolator computes dense output inside the last step computed. The interpolation equation is consistent with the integration scheme :
    
      - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ h [(1 - θ) y' :sub:`1` + θ y' :sub:`2` ]
      - Using reference point at step end:
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) + (1-θ) h [θ y' :sub:`1` - (1+θ) y' :sub:`2` ]
    
    where θ belongs to [0 ; 1] and where y' :sub:`1` and y' :sub:`2` are the two evaluations of the derivatives already computed during the step.
    
          - MidpointFieldIntegrator
    """
    def __init__(self, field: org.hipparchus.Field[_MidpointFieldStateInterpolator__T], forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[_MidpointFieldStateInterpolator__T]], jpype.JArray], globalPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_MidpointFieldStateInterpolator__T], globalCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_MidpointFieldStateInterpolator__T], softPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_MidpointFieldStateInterpolator__T], softCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_MidpointFieldStateInterpolator__T], mapper: org.hipparchus.ode.FieldEquationsMapper[_MidpointFieldStateInterpolator__T]):
        """
        Simple constructor.
        
        Parameters:
            field (hipparchus<MidpointFieldStateInterpolator> field): field to which the time and state vector elements belong
            forward (boolean): integration direction indicator
            yDotK (MidpointFieldStateInterpolator[][]): slopes at the intermediate points
            globalPreviousState (FieldODEStateAndDerivative<MidpointFieldStateInterpolator> globalPreviousState): start of the global step
            globalCurrentState (FieldODEStateAndDerivative<MidpointFieldStateInterpolator> globalCurrentState): end of the global step
            softPreviousState (FieldODEStateAndDerivative<MidpointFieldStateInterpolator> softPreviousState): start of the restricted step
            softCurrentState (FieldODEStateAndDerivative<MidpointFieldStateInterpolator> softCurrentState): end of the restricted step
            mapper (FieldEquationsMapper<MidpointFieldStateInterpolator> mapper): equations mapper for the all equations
        
        
        """
        ...

class MidpointStateInterpolator(RungeKuttaStateInterpolator):
    """
    This class implements a step interpolator for second order Runge-Kutta integrator.
    
    This interpolator computes dense output inside the last step computed. The interpolation equation is consistent with the integration scheme :
    
      - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ h [(1 - θ) y' :sub:`1` + θ y' :sub:`2` ]
      - Using reference point at step end:
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) + (1-θ) h [θ y' :sub:`1` - (1+θ) y' :sub:`2` ]
    
    where θ belongs to [0 ; 1] and where y' :sub:`1` and y' :sub:`2` are the two evaluations of the derivatives already computed during the step.
    
          - MidpointIntegrator
          - serialized
    """
    def __init__(self, forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], globalPreviousState: org.hipparchus.ode.ODEStateAndDerivative, globalCurrentState: org.hipparchus.ode.ODEStateAndDerivative, softPreviousState: org.hipparchus.ode.ODEStateAndDerivative, softCurrentState: org.hipparchus.ode.ODEStateAndDerivative, mapper: org.hipparchus.ode.EquationsMapper):
        """
        Simple constructor.
        
        Parameters:
            forward (boolean): integration direction indicator
            yDotK (double[][]): slopes at the intermediate points
            globalPreviousState (ODEStateAndDerivative): start of the global step
            globalCurrentState (ODEStateAndDerivative): end of the global step
            softPreviousState (ODEStateAndDerivative): start of the restricted step
            softCurrentState (ODEStateAndDerivative): end of the restricted step
            mapper (EquationsMapper): equations mapper for the all equations
        
        
        """
        ...

_ThreeEighthesFieldStateInterpolator__T = typing.TypeVar('_ThreeEighthesFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class ThreeEighthesFieldStateInterpolator(RungeKuttaFieldStateInterpolator[_ThreeEighthesFieldStateInterpolator__T], typing.Generic[_ThreeEighthesFieldStateInterpolator__T]):
    """
    This class implements a step interpolator for the 3/8 fourth order Runge-Kutta integrator.
    
    This interpolator allows to compute dense output inside the last step computed. The interpolation equation is consistent with the integration scheme :
    
      - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ (h/8) [ (8 - 15 θ + 8 θ :sup:`2` ) y' :sub:`1` + 3 * (15 θ - 12 θ
        :sup:`2` ) y' :sub:`2` + 3 θ y' :sub:`3` + (-3 θ + 4 θ :sup:`2` ) y' :sub:`4` ]
      - Using reference point at step end:
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) - (1 - θ) (h/8) [(1 - 7 θ + 8 θ :sup:`2` ) y' :sub:`1` + 3 (1 + θ - 4 θ :sup:`2` ) y' :sub:`2` + 3 (1 + θ) y' :sub:`3` + (1 + θ + 4 θ :sup:`2` ) y' :sub:`4` ]
    
    where θ belongs to [0 ; 1] and where y' :sub:`1` to y' :sub:`4` are the four evaluations of the derivatives already computed during the step.
    
          - ThreeEighthesFieldIntegrator
    """
    def __init__(self, field: org.hipparchus.Field[_ThreeEighthesFieldStateInterpolator__T], forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[_ThreeEighthesFieldStateInterpolator__T]], jpype.JArray], globalPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_ThreeEighthesFieldStateInterpolator__T], globalCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_ThreeEighthesFieldStateInterpolator__T], softPreviousState: org.hipparchus.ode.FieldODEStateAndDerivative[_ThreeEighthesFieldStateInterpolator__T], softCurrentState: org.hipparchus.ode.FieldODEStateAndDerivative[_ThreeEighthesFieldStateInterpolator__T], mapper: org.hipparchus.ode.FieldEquationsMapper[_ThreeEighthesFieldStateInterpolator__T]):
        """
        Simple constructor.
        
        Parameters:
            field (hipparchus<ThreeEighthesFieldStateInterpolator> field): field to which the time and state vector elements belong
            forward (boolean): integration direction indicator
            yDotK (ThreeEighthesFieldStateInterpolator[][]): slopes at the intermediate points
            globalPreviousState (FieldODEStateAndDerivative<ThreeEighthesFieldStateInterpolator> globalPreviousState): start of the global step
            globalCurrentState (FieldODEStateAndDerivative<ThreeEighthesFieldStateInterpolator> globalCurrentState): end of the global step
            softPreviousState (FieldODEStateAndDerivative<ThreeEighthesFieldStateInterpolator> softPreviousState): start of the restricted step
            softCurrentState (FieldODEStateAndDerivative<ThreeEighthesFieldStateInterpolator> softCurrentState): end of the restricted step
            mapper (FieldEquationsMapper<ThreeEighthesFieldStateInterpolator> mapper): equations mapper for the all equations
        
        
        """
        ...

class ThreeEighthesStateInterpolator(RungeKuttaStateInterpolator):
    """
    This class implements a step interpolator for the 3/8 fourth order Runge-Kutta integrator.
    
    This interpolator allows to compute dense output inside the last step computed. The interpolation equation is consistent with the integration scheme :
    
      - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ (h/8) [ (8 - 15 θ + 8 θ :sup:`2` ) y' :sub:`1` + 3 * (15 θ - 12 θ
        :sup:`2` ) y' :sub:`2` + 3 θ y' :sub:`3` + (-3 θ + 4 θ :sup:`2` ) y' :sub:`4` ]
      - Using reference point at step end:
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) - (1 - θ) (h/8) [(1 - 7 θ + 8 θ :sup:`2` ) y' :sub:`1` + 3 (1 + θ - 4 θ :sup:`2` ) y' :sub:`2` + 3 (1 + θ) y' :sub:`3` + (1 + θ + 4 θ :sup:`2` ) y' :sub:`4` ]
    
    where θ belongs to [0 ; 1] and where y' :sub:`1` to y' :sub:`4` are the four evaluations of the derivatives already computed during the step.
    
          - ThreeEighthesIntegrator
          - serialized
    """
    def __init__(self, forward: bool, yDotK: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], globalPreviousState: org.hipparchus.ode.ODEStateAndDerivative, globalCurrentState: org.hipparchus.ode.ODEStateAndDerivative, softPreviousState: org.hipparchus.ode.ODEStateAndDerivative, softCurrentState: org.hipparchus.ode.ODEStateAndDerivative, mapper: org.hipparchus.ode.EquationsMapper):
        """
        Simple constructor.
        
        Parameters:
            forward (boolean): integration direction indicator
            yDotK (double[][]): slopes at the intermediate points
            globalPreviousState (ODEStateAndDerivative): start of the global step
            globalCurrentState (ODEStateAndDerivative): end of the global step
            softPreviousState (ODEStateAndDerivative): start of the restricted step
            softCurrentState (ODEStateAndDerivative): end of the restricted step
            mapper (EquationsMapper): equations mapper for the all equations
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.ode.nonstiff.interpolators")``.

    AdamsFieldStateInterpolator: typing.Type[AdamsFieldStateInterpolator]
    AdamsStateInterpolator: typing.Type[AdamsStateInterpolator]
    ClassicalRungeKuttaFieldStateInterpolator: typing.Type[ClassicalRungeKuttaFieldStateInterpolator]
    ClassicalRungeKuttaStateInterpolator: typing.Type[ClassicalRungeKuttaStateInterpolator]
    DormandPrince54FieldStateInterpolator: typing.Type[DormandPrince54FieldStateInterpolator]
    DormandPrince54StateInterpolator: typing.Type[DormandPrince54StateInterpolator]
    DormandPrince853FieldStateInterpolator: typing.Type[DormandPrince853FieldStateInterpolator]
    DormandPrince853StateInterpolator: typing.Type[DormandPrince853StateInterpolator]
    EulerFieldStateInterpolator: typing.Type[EulerFieldStateInterpolator]
    EulerStateInterpolator: typing.Type[EulerStateInterpolator]
    GillFieldStateInterpolator: typing.Type[GillFieldStateInterpolator]
    GillStateInterpolator: typing.Type[GillStateInterpolator]
    GraggBulirschStoerStateInterpolator: typing.Type[GraggBulirschStoerStateInterpolator]
    HighamHall54FieldStateInterpolator: typing.Type[HighamHall54FieldStateInterpolator]
    HighamHall54StateInterpolator: typing.Type[HighamHall54StateInterpolator]
    LutherFieldStateInterpolator: typing.Type[LutherFieldStateInterpolator]
    LutherStateInterpolator: typing.Type[LutherStateInterpolator]
    MidpointFieldStateInterpolator: typing.Type[MidpointFieldStateInterpolator]
    MidpointStateInterpolator: typing.Type[MidpointStateInterpolator]
    RungeKuttaFieldStateInterpolator: typing.Type[RungeKuttaFieldStateInterpolator]
    RungeKuttaStateInterpolator: typing.Type[RungeKuttaStateInterpolator]
    ThreeEighthesFieldStateInterpolator: typing.Type[ThreeEighthesFieldStateInterpolator]
    ThreeEighthesStateInterpolator: typing.Type[ThreeEighthesStateInterpolator]
