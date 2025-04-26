
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
    public classAdamsFieldStateInterpolator<T extends :class:`~org.hipparchus.ode.nonstiff.interpolators.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.sampling.AbstractFieldODEStateInterpolator`<T>
    
        This class implements an interpolator for Adams integrators using Nordsieck representation.
    
        This interpolator computes dense output around the current point. The interpolation equation is based on Taylor series
        formulas.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.AdamsBashforthFieldIntegrator`
              - :class:`~org.hipparchus.ode.nonstiff.AdamsMoultonFieldIntegrator`
    """
    def __init__(self, t: _AdamsFieldStateInterpolator__T, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_AdamsFieldStateInterpolator__T], tArray: typing.Union[typing.List[_AdamsFieldStateInterpolator__T], jpype.JArray], array2DRowFieldMatrix: org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsFieldStateInterpolator__T], boolean: bool, fieldODEStateAndDerivative2: org.hipparchus.ode.FieldODEStateAndDerivative[_AdamsFieldStateInterpolator__T], fieldODEStateAndDerivative3: org.hipparchus.ode.FieldODEStateAndDerivative[_AdamsFieldStateInterpolator__T], fieldEquationsMapper: org.hipparchus.ode.FieldEquationsMapper[_AdamsFieldStateInterpolator__T]): ...
    def getNordsieck(self) -> org.hipparchus.linear.Array2DRowFieldMatrix[_AdamsFieldStateInterpolator__T]: ...
    def getScaled(self) -> typing.MutableSequence[_AdamsFieldStateInterpolator__T]:
        """
            Get the first scaled derivative.
        
            Returns:
                first scaled derivative
        
        
        """
        ...
    _taylor__S = typing.TypeVar('_taylor__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    @staticmethod
    def taylor(fieldEquationsMapper: org.hipparchus.ode.FieldEquationsMapper[_taylor__S], fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_taylor__S], s: _taylor__S, s2: _taylor__S, sArray: typing.Union[typing.List[_taylor__S], jpype.JArray], array2DRowFieldMatrix: org.hipparchus.linear.Array2DRowFieldMatrix[_taylor__S]) -> org.hipparchus.ode.FieldODEStateAndDerivative[_taylor__S]:
        """
            Estimate state by applying Taylor formula.
        
            Parameters:
                equationsMapper (:class:`~org.hipparchus.ode.FieldEquationsMapper`<S> equationsMapper): mapper for ODE equations primary and secondary components
                reference (:class:`~org.hipparchus.ode.FieldODEStateAndDerivative`<S> reference): reference state
                time (S): time at which state must be estimated
                stepSize (S): step size used in the scaled and Nordsieck arrays
                scaled (S[]): first scaled derivative
                nordsieck (:class:`~org.hipparchus.ode.nonstiff.interpolators.https:.www.hipparchus.org.hipparchus`<S> nordsieck): Nordsieck vector
        
            Returns:
                estimated state
        
        
        """
        ...

class AdamsStateInterpolator(org.hipparchus.ode.sampling.AbstractODEStateInterpolator):
    """
    public classAdamsStateInterpolator extends :class:`~org.hipparchus.ode.sampling.AbstractODEStateInterpolator`
    
        This class implements an interpolator for integrators using Nordsieck representation.
    
        This interpolator computes dense output around the current point. The interpolation equation is based on Taylor series
        formulas.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.AdamsBashforthIntegrator`
              - :class:`~org.hipparchus.ode.nonstiff.AdamsMoultonIntegrator`
              - :meth:`~serialized`
    """
    def __init__(self, double: float, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, doubleArray: typing.Union[typing.List[float], jpype.JArray], array2DRowRealMatrix: org.hipparchus.linear.Array2DRowRealMatrix, boolean: bool, oDEStateAndDerivative2: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative3: org.hipparchus.ode.ODEStateAndDerivative, equationsMapper: org.hipparchus.ode.EquationsMapper): ...
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
    def taylor(equationsMapper: org.hipparchus.ode.EquationsMapper, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float, double2: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], array2DRowRealMatrix: org.hipparchus.linear.Array2DRowRealMatrix) -> org.hipparchus.ode.ODEStateAndDerivative:
        """
            Estimate state by applying Taylor formula.
        
            Parameters:
                equationsMapper (:class:`~org.hipparchus.ode.EquationsMapper`): mapper for ODE equations primary and secondary components
                reference (:class:`~org.hipparchus.ode.ODEStateAndDerivative`): reference state
                time (double): time at which state must be estimated
                stepSize (double): step size used in the scaled and Nordsieck arrays
                scaled (double[]): first scaled derivative
                nordsieck (:class:`~org.hipparchus.ode.nonstiff.interpolators.https:.www.hipparchus.org.hipparchus`): Nordsieck vector
        
            Returns:
                estimated state
        
        
        """
        ...

class GraggBulirschStoerStateInterpolator(org.hipparchus.ode.sampling.AbstractODEStateInterpolator):
    """
    public classGraggBulirschStoerStateInterpolator extends :class:`~org.hipparchus.ode.sampling.AbstractODEStateInterpolator`
    
        This class implements an interpolator for the Gragg-Bulirsch-Stoer integrator.
    
        This interpolator compute dense output inside the last step produced by a Gragg-Bulirsch-Stoer integrator.
    
        This implementation is basically a reimplementation in Java of the `odex
        <http://www.unige.ch/math/folks/hairer/prog/nonstiff/odex.f>` fortran code by E. Hairer and G. Wanner. The
        redistribution policy for this code is available `here <http://www.unige.ch/~hairer/prog/licence.txt>`, for convenience,
        it is reproduced below.
    
            Copyright (c) 2004, Ernst Hairer
    
            Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
            following conditions are met:
    
              - Redistributions of source code must retain the above copyright notice, this list of conditions and the following
                disclaimer.
              - Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
                disclaimer in the documentation and/or other materials provided with the distribution.
    
    
            **THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
            INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
            DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
            EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
            USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
            STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
            IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.**
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.GraggBulirschStoerIntegrator`
              - :meth:`~serialized`
    """
    def __init__(self, boolean: bool, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative2: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative3: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative4: org.hipparchus.ode.ODEStateAndDerivative, equationsMapper: org.hipparchus.ode.EquationsMapper, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int: int): ...
    def estimateError(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
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
    public abstract classRungeKuttaFieldStateInterpolator<T extends :class:`~org.hipparchus.ode.nonstiff.interpolators.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.sampling.AbstractFieldODEStateInterpolator`<T>
    
        This class represents an interpolator over the last step during an ODE integration for Runge-Kutta and embedded
        Runge-Kutta integrators.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.FixedStepRungeKuttaFieldIntegrator`
              - :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaFieldIntegrator`
    """
    ...

class RungeKuttaStateInterpolator(org.hipparchus.ode.sampling.AbstractODEStateInterpolator):
    """
    public abstract classRungeKuttaStateInterpolator extends :class:`~org.hipparchus.ode.sampling.AbstractODEStateInterpolator`
    
        This class represents an interpolator over the last step during an ODE integration for Runge-Kutta and embedded
        Runge-Kutta integrators.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.FixedStepRungeKuttaIntegrator`
              - :class:`~org.hipparchus.ode.nonstiff.EmbeddedRungeKuttaIntegrator`
              - :meth:`~serialized`
    """
    ...

_ClassicalRungeKuttaFieldStateInterpolator__T = typing.TypeVar('_ClassicalRungeKuttaFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class ClassicalRungeKuttaFieldStateInterpolator(RungeKuttaFieldStateInterpolator[_ClassicalRungeKuttaFieldStateInterpolator__T], typing.Generic[_ClassicalRungeKuttaFieldStateInterpolator__T]):
    """
    public classClassicalRungeKuttaFieldStateInterpolator<T extends :class:`~org.hipparchus.ode.nonstiff.interpolators.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaFieldStateInterpolator`<T>
    
        This class implements a step interpolator for the classical fourth order Runge-Kutta integrator.
    
        This interpolator allows to compute dense output inside the last step computed. The interpolation equation is consistent
        with the integration scheme :
    
          - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ (h/6) [ (6 - 9 θ + 4 θ :sup:`2` ) y' :sub:`1` + ( 6 θ - 4 θ :sup:`2` )
            (y' :sub:`2` + y' :sub:`3` ) + ( -3 θ + 4 θ :sup:`2` ) y' :sub:`4` ]
          - Using reference point at step end:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) + (1 - θ) (h/6) [ (-4 θ^2 + 5 θ - 1) y' :sub:`1` +(4 θ^2 - 2 θ - 2) (y'
            :sub:`2` + y' :sub:`3` ) -(4 θ^2 + θ + 1) y' :sub:`4` ]
    
    
        where θ belongs to [0 ; 1] and where y' :sub:`1` to y' :sub:`4` are the four evaluations of the derivatives already
        computed during the step.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaFieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_ClassicalRungeKuttaFieldStateInterpolator__T], boolean: bool, tArray: typing.Union[typing.List[typing.MutableSequence[_ClassicalRungeKuttaFieldStateInterpolator__T]], jpype.JArray], fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_ClassicalRungeKuttaFieldStateInterpolator__T], fieldODEStateAndDerivative2: org.hipparchus.ode.FieldODEStateAndDerivative[_ClassicalRungeKuttaFieldStateInterpolator__T], fieldODEStateAndDerivative3: org.hipparchus.ode.FieldODEStateAndDerivative[_ClassicalRungeKuttaFieldStateInterpolator__T], fieldODEStateAndDerivative4: org.hipparchus.ode.FieldODEStateAndDerivative[_ClassicalRungeKuttaFieldStateInterpolator__T], fieldEquationsMapper: org.hipparchus.ode.FieldEquationsMapper[_ClassicalRungeKuttaFieldStateInterpolator__T]): ...

class ClassicalRungeKuttaStateInterpolator(RungeKuttaStateInterpolator):
    """
    public classClassicalRungeKuttaStateInterpolator extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaStateInterpolator`
    
        This class implements a step interpolator for the classical fourth order Runge-Kutta integrator.
    
        This interpolator allows to compute dense output inside the last step computed. The interpolation equation is consistent
        with the integration scheme :
    
          - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ (h/6) [ (6 - 9 θ + 4 θ :sup:`2` ) y' :sub:`1` + ( 6 θ - 4 θ :sup:`2` )
            (y' :sub:`2` + y' :sub:`3` ) + ( -3 θ + 4 θ :sup:`2` ) y' :sub:`4` ]
          - Using reference point at step end:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) + (1 - θ) (h/6) [ (-4 θ^2 + 5 θ - 1) y' :sub:`1` +(4 θ^2 - 2 θ - 2) (y'
            :sub:`2` + y' :sub:`3` ) -(4 θ^2 + θ + 1) y' :sub:`4` ]
    
    
        where θ belongs to [0 ; 1] and where y' :sub:`1` to y' :sub:`4` are the four evaluations of the derivatives already
        computed during the step.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator`
              - :meth:`~serialized`
    """
    def __init__(self, boolean: bool, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative2: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative3: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative4: org.hipparchus.ode.ODEStateAndDerivative, equationsMapper: org.hipparchus.ode.EquationsMapper): ...

_DormandPrince54FieldStateInterpolator__T = typing.TypeVar('_DormandPrince54FieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class DormandPrince54FieldStateInterpolator(RungeKuttaFieldStateInterpolator[_DormandPrince54FieldStateInterpolator__T], typing.Generic[_DormandPrince54FieldStateInterpolator__T]):
    """
    public classDormandPrince54FieldStateInterpolator<T extends :class:`~org.hipparchus.ode.nonstiff.interpolators.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaFieldStateInterpolator`<T>
    
        This class represents an interpolator over the last step during an ODE integration for the 5(4) Dormand-Prince
        integrator.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.DormandPrince54Integrator`
    """
    def __init__(self, field: org.hipparchus.Field[_DormandPrince54FieldStateInterpolator__T], boolean: bool, tArray: typing.Union[typing.List[typing.MutableSequence[_DormandPrince54FieldStateInterpolator__T]], jpype.JArray], fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince54FieldStateInterpolator__T], fieldODEStateAndDerivative2: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince54FieldStateInterpolator__T], fieldODEStateAndDerivative3: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince54FieldStateInterpolator__T], fieldODEStateAndDerivative4: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince54FieldStateInterpolator__T], fieldEquationsMapper: org.hipparchus.ode.FieldEquationsMapper[_DormandPrince54FieldStateInterpolator__T]): ...

class DormandPrince54StateInterpolator(RungeKuttaStateInterpolator):
    """
    public classDormandPrince54StateInterpolator extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaStateInterpolator`
    
        This class represents an interpolator over the last step during an ODE integration for the 5(4) Dormand-Prince
        integrator.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.DormandPrince54Integrator`
              - :meth:`~serialized`
    """
    def __init__(self, boolean: bool, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative2: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative3: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative4: org.hipparchus.ode.ODEStateAndDerivative, equationsMapper: org.hipparchus.ode.EquationsMapper): ...

_DormandPrince853FieldStateInterpolator__T = typing.TypeVar('_DormandPrince853FieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class DormandPrince853FieldStateInterpolator(RungeKuttaFieldStateInterpolator[_DormandPrince853FieldStateInterpolator__T], typing.Generic[_DormandPrince853FieldStateInterpolator__T]):
    """
    public classDormandPrince853FieldStateInterpolator<T extends :class:`~org.hipparchus.ode.nonstiff.interpolators.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaFieldStateInterpolator`<T>
    
        This class represents an interpolator over the last step during an ODE integration for the 8(5,3) Dormand-Prince
        integrator.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.DormandPrince853FieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_DormandPrince853FieldStateInterpolator__T], boolean: bool, tArray: typing.Union[typing.List[typing.MutableSequence[_DormandPrince853FieldStateInterpolator__T]], jpype.JArray], fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince853FieldStateInterpolator__T], fieldODEStateAndDerivative2: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince853FieldStateInterpolator__T], fieldODEStateAndDerivative3: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince853FieldStateInterpolator__T], fieldODEStateAndDerivative4: org.hipparchus.ode.FieldODEStateAndDerivative[_DormandPrince853FieldStateInterpolator__T], fieldEquationsMapper: org.hipparchus.ode.FieldEquationsMapper[_DormandPrince853FieldStateInterpolator__T]): ...

class DormandPrince853StateInterpolator(RungeKuttaStateInterpolator):
    """
    public classDormandPrince853StateInterpolator extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaStateInterpolator`
    
        This class represents an interpolator over the last step during an ODE integration for the 8(5,3) Dormand-Prince
        integrator.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.DormandPrince853Integrator`
              - :meth:`~serialized`
    """
    def __init__(self, boolean: bool, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative2: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative3: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative4: org.hipparchus.ode.ODEStateAndDerivative, equationsMapper: org.hipparchus.ode.EquationsMapper): ...

_EulerFieldStateInterpolator__T = typing.TypeVar('_EulerFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class EulerFieldStateInterpolator(RungeKuttaFieldStateInterpolator[_EulerFieldStateInterpolator__T], typing.Generic[_EulerFieldStateInterpolator__T]):
    """
    public classEulerFieldStateInterpolator<T extends :class:`~org.hipparchus.ode.nonstiff.interpolators.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaFieldStateInterpolator`<T>
    
        This class implements a linear interpolator for step.
    
        This interpolator computes dense output inside the last step computed. The interpolation equation is consistent with the
        integration scheme :
    
          - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ h y'
          - Using reference point at step end:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) - (1-θ) h y'
    
    
        where θ belongs to [0 ; 1] and where y' is the evaluation of the derivatives already computed during the step.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.EulerFieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_EulerFieldStateInterpolator__T], boolean: bool, tArray: typing.Union[typing.List[typing.MutableSequence[_EulerFieldStateInterpolator__T]], jpype.JArray], fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_EulerFieldStateInterpolator__T], fieldODEStateAndDerivative2: org.hipparchus.ode.FieldODEStateAndDerivative[_EulerFieldStateInterpolator__T], fieldODEStateAndDerivative3: org.hipparchus.ode.FieldODEStateAndDerivative[_EulerFieldStateInterpolator__T], fieldODEStateAndDerivative4: org.hipparchus.ode.FieldODEStateAndDerivative[_EulerFieldStateInterpolator__T], fieldEquationsMapper: org.hipparchus.ode.FieldEquationsMapper[_EulerFieldStateInterpolator__T]): ...

class EulerStateInterpolator(RungeKuttaStateInterpolator):
    """
    public classEulerStateInterpolator extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaStateInterpolator`
    
        This class implements a linear interpolator for step.
    
        This interpolator computes dense output inside the last step computed. The interpolation equation is consistent with the
        integration scheme :
    
          - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ h y'
          - Using reference point at step end:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) - (1-θ) h y'
    
    
        where θ belongs to [0 ; 1] and where y' is the evaluation of the derivatives already computed during the step.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.EulerIntegrator`
              - :meth:`~serialized`
    """
    def __init__(self, boolean: bool, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative2: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative3: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative4: org.hipparchus.ode.ODEStateAndDerivative, equationsMapper: org.hipparchus.ode.EquationsMapper): ...

_GillFieldStateInterpolator__T = typing.TypeVar('_GillFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class GillFieldStateInterpolator(RungeKuttaFieldStateInterpolator[_GillFieldStateInterpolator__T], typing.Generic[_GillFieldStateInterpolator__T]):
    """
    public classGillFieldStateInterpolator<T extends :class:`~org.hipparchus.ode.nonstiff.interpolators.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaFieldStateInterpolator`<T>
    
        This class implements a step interpolator for the Gill fourth order Runge-Kutta integrator.
    
        This interpolator allows to compute dense output inside the last step computed. The interpolation equation is consistent
        with the integration scheme :
    
          - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ (h/6) [ (6 - 9 θ + 4 θ :sup:`2` ) y' :sub:`1` + ( 6 θ - 4 θ :sup:`2` )
            ((1-1/√2) y' :sub:`2` + (1+1/√2)) y' :sub:`3` ) + ( - 3 θ + 4 θ :sup:`2` ) y' :sub:`4` ]
          - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) - (1 - θ) (h/6) [ (1 - 5 θ + 4 θ :sup:`2` ) y' :sub:`1` + (2 + 2 θ - 4 θ
            :sup:`2` ) ((1-1/√2) y' :sub:`2` + (1+1/√2)) y' :sub:`3` ) + (1 + θ + 4 θ :sup:`2` ) y' :sub:`4` ]
    
    
        where θ belongs to [0 ; 1] and where y' :sub:`1` to y' :sub:`4` are the four evaluations of the derivatives already
        computed during the step.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.GillFieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_GillFieldStateInterpolator__T], boolean: bool, tArray: typing.Union[typing.List[typing.MutableSequence[_GillFieldStateInterpolator__T]], jpype.JArray], fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_GillFieldStateInterpolator__T], fieldODEStateAndDerivative2: org.hipparchus.ode.FieldODEStateAndDerivative[_GillFieldStateInterpolator__T], fieldODEStateAndDerivative3: org.hipparchus.ode.FieldODEStateAndDerivative[_GillFieldStateInterpolator__T], fieldODEStateAndDerivative4: org.hipparchus.ode.FieldODEStateAndDerivative[_GillFieldStateInterpolator__T], fieldEquationsMapper: org.hipparchus.ode.FieldEquationsMapper[_GillFieldStateInterpolator__T]): ...

class GillStateInterpolator(RungeKuttaStateInterpolator):
    """
    public classGillStateInterpolator extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaStateInterpolator`
    
        This class implements a step interpolator for the Gill fourth order Runge-Kutta integrator.
    
        This interpolator allows to compute dense output inside the last step computed. The interpolation equation is consistent
        with the integration scheme :
    
          - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ (h/6) [ (6 - 9 θ + 4 θ :sup:`2` ) y' :sub:`1` + ( 6 θ - 4 θ :sup:`2` )
            ((1-1/√2) y' :sub:`2` + (1+1/√2)) y' :sub:`3` ) + ( - 3 θ + 4 θ :sup:`2` ) y' :sub:`4` ]
          - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) - (1 - θ) (h/6) [ (1 - 5 θ + 4 θ :sup:`2` ) y' :sub:`1` + (2 + 2 θ - 4 θ
            :sup:`2` ) ((1-1/√2) y' :sub:`2` + (1+1/√2)) y' :sub:`3` ) + (1 + θ + 4 θ :sup:`2` ) y' :sub:`4` ]
    
    
        where θ belongs to [0 ; 1] and where y' :sub:`1` to y' :sub:`4` are the four evaluations of the derivatives already
        computed during the step.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.GillIntegrator`
              - :meth:`~serialized`
    """
    def __init__(self, boolean: bool, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative2: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative3: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative4: org.hipparchus.ode.ODEStateAndDerivative, equationsMapper: org.hipparchus.ode.EquationsMapper): ...

_HighamHall54FieldStateInterpolator__T = typing.TypeVar('_HighamHall54FieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class HighamHall54FieldStateInterpolator(RungeKuttaFieldStateInterpolator[_HighamHall54FieldStateInterpolator__T], typing.Generic[_HighamHall54FieldStateInterpolator__T]):
    """
    public classHighamHall54FieldStateInterpolator<T extends :class:`~org.hipparchus.ode.nonstiff.interpolators.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaFieldStateInterpolator`<T>
    
        This class represents an interpolator over the last step during an ODE integration for the 5(4) Higham and Hall
        integrator.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.HighamHall54FieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_HighamHall54FieldStateInterpolator__T], boolean: bool, tArray: typing.Union[typing.List[typing.MutableSequence[_HighamHall54FieldStateInterpolator__T]], jpype.JArray], fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_HighamHall54FieldStateInterpolator__T], fieldODEStateAndDerivative2: org.hipparchus.ode.FieldODEStateAndDerivative[_HighamHall54FieldStateInterpolator__T], fieldODEStateAndDerivative3: org.hipparchus.ode.FieldODEStateAndDerivative[_HighamHall54FieldStateInterpolator__T], fieldODEStateAndDerivative4: org.hipparchus.ode.FieldODEStateAndDerivative[_HighamHall54FieldStateInterpolator__T], fieldEquationsMapper: org.hipparchus.ode.FieldEquationsMapper[_HighamHall54FieldStateInterpolator__T]): ...

class HighamHall54StateInterpolator(RungeKuttaStateInterpolator):
    """
    public classHighamHall54StateInterpolator extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaStateInterpolator`
    
        This class represents an interpolator over the last step during an ODE integration for the 5(4) Higham and Hall
        integrator.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.HighamHall54Integrator`
              - :meth:`~serialized`
    """
    def __init__(self, boolean: bool, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative2: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative3: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative4: org.hipparchus.ode.ODEStateAndDerivative, equationsMapper: org.hipparchus.ode.EquationsMapper): ...

_LutherFieldStateInterpolator__T = typing.TypeVar('_LutherFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class LutherFieldStateInterpolator(RungeKuttaFieldStateInterpolator[_LutherFieldStateInterpolator__T], typing.Generic[_LutherFieldStateInterpolator__T]):
    """
    public classLutherFieldStateInterpolator<T extends :class:`~org.hipparchus.ode.nonstiff.interpolators.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaFieldStateInterpolator`<T>
    
        This class represents an interpolator over the last step during an ODE integration for the 6th order Luther integrator.
    
        This interpolator computes dense output inside the last step computed. The interpolation equation is consistent with the
        integration scheme.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.LutherFieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_LutherFieldStateInterpolator__T], boolean: bool, tArray: typing.Union[typing.List[typing.MutableSequence[_LutherFieldStateInterpolator__T]], jpype.JArray], fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_LutherFieldStateInterpolator__T], fieldODEStateAndDerivative2: org.hipparchus.ode.FieldODEStateAndDerivative[_LutherFieldStateInterpolator__T], fieldODEStateAndDerivative3: org.hipparchus.ode.FieldODEStateAndDerivative[_LutherFieldStateInterpolator__T], fieldODEStateAndDerivative4: org.hipparchus.ode.FieldODEStateAndDerivative[_LutherFieldStateInterpolator__T], fieldEquationsMapper: org.hipparchus.ode.FieldEquationsMapper[_LutherFieldStateInterpolator__T]): ...

class LutherStateInterpolator(RungeKuttaStateInterpolator):
    """
    public classLutherStateInterpolator extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaStateInterpolator`
    
        This class represents an interpolator over the last step during an ODE integration for the 6th order Luther integrator.
    
        This interpolator computes dense output inside the last step computed. The interpolation equation is consistent with the
        integration scheme.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.LutherIntegrator`
              - :meth:`~serialized`
    """
    def __init__(self, boolean: bool, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative2: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative3: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative4: org.hipparchus.ode.ODEStateAndDerivative, equationsMapper: org.hipparchus.ode.EquationsMapper): ...

_MidpointFieldStateInterpolator__T = typing.TypeVar('_MidpointFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class MidpointFieldStateInterpolator(RungeKuttaFieldStateInterpolator[_MidpointFieldStateInterpolator__T], typing.Generic[_MidpointFieldStateInterpolator__T]):
    """
    public classMidpointFieldStateInterpolator<T extends :class:`~org.hipparchus.ode.nonstiff.interpolators.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaFieldStateInterpolator`<T>
    
        This class implements a step interpolator for second order Runge-Kutta integrator.
    
        This interpolator computes dense output inside the last step computed. The interpolation equation is consistent with the
        integration scheme :
    
          - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ h [(1 - θ) y' :sub:`1` + θ y' :sub:`2` ]
          - Using reference point at step end:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) + (1-θ) h [θ y' :sub:`1` - (1+θ) y' :sub:`2` ]
    
    
        where θ belongs to [0 ; 1] and where y' :sub:`1` and y' :sub:`2` are the two evaluations of the derivatives already
        computed during the step.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.MidpointFieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_MidpointFieldStateInterpolator__T], boolean: bool, tArray: typing.Union[typing.List[typing.MutableSequence[_MidpointFieldStateInterpolator__T]], jpype.JArray], fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_MidpointFieldStateInterpolator__T], fieldODEStateAndDerivative2: org.hipparchus.ode.FieldODEStateAndDerivative[_MidpointFieldStateInterpolator__T], fieldODEStateAndDerivative3: org.hipparchus.ode.FieldODEStateAndDerivative[_MidpointFieldStateInterpolator__T], fieldODEStateAndDerivative4: org.hipparchus.ode.FieldODEStateAndDerivative[_MidpointFieldStateInterpolator__T], fieldEquationsMapper: org.hipparchus.ode.FieldEquationsMapper[_MidpointFieldStateInterpolator__T]): ...

class MidpointStateInterpolator(RungeKuttaStateInterpolator):
    """
    public classMidpointStateInterpolator extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaStateInterpolator`
    
        This class implements a step interpolator for second order Runge-Kutta integrator.
    
        This interpolator computes dense output inside the last step computed. The interpolation equation is consistent with the
        integration scheme :
    
          - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ h [(1 - θ) y' :sub:`1` + θ y' :sub:`2` ]
          - Using reference point at step end:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) + (1-θ) h [θ y' :sub:`1` - (1+θ) y' :sub:`2` ]
    
    
        where θ belongs to [0 ; 1] and where y' :sub:`1` and y' :sub:`2` are the two evaluations of the derivatives already
        computed during the step.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.MidpointIntegrator`
              - :meth:`~serialized`
    """
    def __init__(self, boolean: bool, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative2: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative3: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative4: org.hipparchus.ode.ODEStateAndDerivative, equationsMapper: org.hipparchus.ode.EquationsMapper): ...

_ThreeEighthesFieldStateInterpolator__T = typing.TypeVar('_ThreeEighthesFieldStateInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class ThreeEighthesFieldStateInterpolator(RungeKuttaFieldStateInterpolator[_ThreeEighthesFieldStateInterpolator__T], typing.Generic[_ThreeEighthesFieldStateInterpolator__T]):
    """
    public classThreeEighthesFieldStateInterpolator<T extends :class:`~org.hipparchus.ode.nonstiff.interpolators.https:.www.hipparchus.org.hipparchus`<T>> extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaFieldStateInterpolator`<T>
    
        This class implements a step interpolator for the 3/8 fourth order Runge-Kutta integrator.
    
        This interpolator allows to compute dense output inside the last step computed. The interpolation equation is consistent
        with the integration scheme :
    
          - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ (h/8) [ (8 - 15 θ + 8 θ :sup:`2` ) y' :sub:`1` + 3 * (15 θ - 12 θ
            :sup:`2` ) y' :sub:`2` + 3 θ y' :sub:`3` + (-3 θ + 4 θ :sup:`2` ) y' :sub:`4` ]
          - Using reference point at step end:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) - (1 - θ) (h/8) [(1 - 7 θ + 8 θ :sup:`2` ) y' :sub:`1` + 3 (1 + θ - 4 θ
            :sup:`2` ) y' :sub:`2` + 3 (1 + θ) y' :sub:`3` + (1 + θ + 4 θ :sup:`2` ) y' :sub:`4` ]
    
    
        where θ belongs to [0 ; 1] and where y' :sub:`1` to y' :sub:`4` are the four evaluations of the derivatives already
        computed during the step.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.ThreeEighthesFieldIntegrator`
    """
    def __init__(self, field: org.hipparchus.Field[_ThreeEighthesFieldStateInterpolator__T], boolean: bool, tArray: typing.Union[typing.List[typing.MutableSequence[_ThreeEighthesFieldStateInterpolator__T]], jpype.JArray], fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_ThreeEighthesFieldStateInterpolator__T], fieldODEStateAndDerivative2: org.hipparchus.ode.FieldODEStateAndDerivative[_ThreeEighthesFieldStateInterpolator__T], fieldODEStateAndDerivative3: org.hipparchus.ode.FieldODEStateAndDerivative[_ThreeEighthesFieldStateInterpolator__T], fieldODEStateAndDerivative4: org.hipparchus.ode.FieldODEStateAndDerivative[_ThreeEighthesFieldStateInterpolator__T], fieldEquationsMapper: org.hipparchus.ode.FieldEquationsMapper[_ThreeEighthesFieldStateInterpolator__T]): ...

class ThreeEighthesStateInterpolator(RungeKuttaStateInterpolator):
    """
    public classThreeEighthesStateInterpolator extends :class:`~org.hipparchus.ode.nonstiff.interpolators.RungeKuttaStateInterpolator`
    
        This class implements a step interpolator for the 3/8 fourth order Runge-Kutta integrator.
    
        This interpolator allows to compute dense output inside the last step computed. The interpolation equation is consistent
        with the integration scheme :
    
          - Using reference point at step start:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` ) + θ (h/8) [ (8 - 15 θ + 8 θ :sup:`2` ) y' :sub:`1` + 3 * (15 θ - 12 θ
            :sup:`2` ) y' :sub:`2` + 3 θ y' :sub:`3` + (-3 θ + 4 θ :sup:`2` ) y' :sub:`4` ]
          - Using reference point at step end:
    
    
    y(t :sub:`n` + θ h) = y (t :sub:`n` + h) - (1 - θ) (h/8) [(1 - 7 θ + 8 θ :sup:`2` ) y' :sub:`1` + 3 (1 + θ - 4 θ
            :sup:`2` ) y' :sub:`2` + 3 (1 + θ) y' :sub:`3` + (1 + θ + 4 θ :sup:`2` ) y' :sub:`4` ]
    
    
        where θ belongs to [0 ; 1] and where y' :sub:`1` to y' :sub:`4` are the four evaluations of the derivatives already
        computed during the step.
    
        Also see:
    
              - :class:`~org.hipparchus.ode.nonstiff.ThreeEighthesIntegrator`
              - :meth:`~serialized`
    """
    def __init__(self, boolean: bool, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative2: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative3: org.hipparchus.ode.ODEStateAndDerivative, oDEStateAndDerivative4: org.hipparchus.ode.ODEStateAndDerivative, equationsMapper: org.hipparchus.ode.EquationsMapper): ...


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
