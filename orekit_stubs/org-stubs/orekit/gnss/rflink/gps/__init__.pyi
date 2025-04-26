
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.gnss.metric.parser
import typing



class SubFrame:
    """
    public abstract class SubFrame extends :class:`~org.orekit.gnss.rflink.gps.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for sub-frames in a GPS navigation message.
    
        Since:
            12.0
    """
    PREAMBLE_VALUE: typing.ClassVar[int] = ...
    """
    public static final int PREAMBLE_VALUE
    
        TLM preamble.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def checkParity(int: int, int2: int) -> bool:
        """
            Check parity.
        
            This implements algorithm in table 20-XIV from IS-GPS-200N
        
            Parameters:
                previous (int): previous 30 bits word (only two least significant bits are used)
                current (int): current 30 bits word
        
            Returns:
                true if parity check succeeded
        
        
        """
        ...
    def getAlert(self) -> int:
        """
            Get alert flag.
        
            Returns:
                alert flag
        
        
        """
        ...
    def getAntiSpoofing(self) -> int:
        """
            Get anti-spoofing flag.
        
            Returns:
                anti-spoofing flag
        
        
        """
        ...
    def getId(self) -> int:
        """
            Get sub-frame id.
        
            Returns:
                sub-frame id
        
        
        """
        ...
    def getIntegrityStatus(self) -> int:
        """
            Get integrity status flag.
        
            Returns:
                integrity status flag
        
        
        """
        ...
    def getMessage(self) -> int:
        """
            Get telemetry message.
        
            Returns:
                telemetry message
        
        
        """
        ...
    def getPreamble(self) -> int:
        """
            Get telemetry preamble.
        
            Returns:
                telemetry preamble
        
        
        """
        ...
    def getTow(self) -> int:
        """
            Get Time Of Week of next 12 second message.
        
            Returns:
                Time Of Week of next 12 second message (s)
        
        
        """
        ...
    def hasParityErrors(self) -> bool:
        """
            Check if the sub-frame has parity errors.
        
            Returns:
                true if frame has parity errors
        
        
        """
        ...
    @staticmethod
    def parse(encodedMessage: typing.Union[org.orekit.gnss.metric.parser.EncodedMessage, typing.Callable]) -> 'SubFrame':
        """
            Builder for sub-frames.
        
            This builder creates the proper sub-frame type corresponding to the ID in handover word and the SV Id for sub-frames 4
            and 5.
        
            Parameters:
                encodedMessage (:class:`~org.orekit.gnss.metric.parser.EncodedMessage`): encoded message containing exactly one sub-frame
        
            Returns:
                sub-frame with TLM and HOW fields already set up
        
            Also see:
                :class:`~org.orekit.gnss.rflink.gps.SubFrame1`, :class:`~org.orekit.gnss.rflink.gps.SubFrame2`,
                :class:`~org.orekit.gnss.rflink.gps.SubFrame3`, :class:`~org.orekit.gnss.rflink.gps.SubFrame4A0`,
                :class:`~org.orekit.gnss.rflink.gps.SubFrame4A1`, :class:`~org.orekit.gnss.rflink.gps.SubFrame4B`,
                :class:`~org.orekit.gnss.rflink.gps.SubFrame4C`, :class:`~org.orekit.gnss.rflink.gps.SubFrame4D`,
                :class:`~org.orekit.gnss.rflink.gps.SubFrame4E`, :class:`~org.orekit.gnss.rflink.gps.SubFrameAlmanac`,
                :class:`~org.orekit.gnss.rflink.gps.SubFrameDummyAlmanac`
        
        
        """
        ...

class SubFrame1(SubFrame):
    """
    public class SubFrame1 extends :class:`~org.orekit.gnss.rflink.gps.SubFrame`
    
        Container for sub-frames 1.
    
        Table 20-1, sheet 1 and table 40-1, sheet 1 in
        :class:`~org.orekit.gnss.rflink.gps.https:.navcen.uscg.gov.sites.default.files.pdf.gps.IS`, IS-GPS-200N, 22 Aug 2022
    
        Since:
            12.0
    """
    def getAF0(self) -> float:
        """
            Get af₀.
        
            Returns:
                af₀
        
        
        """
        ...
    def getAF1(self) -> float:
        """
            Get af₁.
        
            Returns:
                af₁ (second/second)
        
        
        """
        ...
    def getAF2(self) -> float:
        """
            Get af₂.
        
            Returns:
                af₂ (second/second²)
        
        
        """
        ...
    def getCaOrPFlag(self) -> int:
        """
            Get C/A or P flag.
        
            Returns:
                C/A or P flag
        
        
        """
        ...
    def getIODC(self) -> int:
        """
            Get IODC.
        
            Returns:
                IODC
        
        
        """
        ...
    def getL2PDataFlag(self) -> int:
        """
            Get L2 P data flag.
        
            Returns:
                L2 P data flag
        
        
        """
        ...
    def getReserved04(self) -> int:
        """
            Get the reserved field in word 4.
        
            Returns:
                reserved field in word 4
        
        
        """
        ...
    def getReserved05(self) -> int:
        """
            Get the reserved field in word 5.
        
            Returns:
                reserved field in word 5
        
        
        """
        ...
    def getReserved06(self) -> int:
        """
            Get the reserved field in word 6.
        
            Returns:
                reserved field in word 6
        
        
        """
        ...
    def getReserved07(self) -> int:
        """
            Get the reserved field in word 7.
        
            Returns:
                reserved field in word 7
        
        
        """
        ...
    def getSvHealth(self) -> int:
        """
            Get SV health.
        
            Returns:
                SV health
        
        
        """
        ...
    def getTGD(self) -> int:
        """
            Get the TGD.
        
            Returns:
                TGD
        
        
        """
        ...
    def getTOC(self) -> int:
        """
            Get the TOC.
        
            Returns:
                TOC
        
        
        """
        ...
    def getUraIndex(self) -> int:
        """
            Get URA index.
        
            Returns:
                URA index
        
        
        """
        ...
    def getWeekNumber(self) -> int:
        """
            Get Week Number.
        
            Returns:
                week number
        
        
        """
        ...

class SubFrame2(SubFrame):
    """
    public class SubFrame2 extends :class:`~org.orekit.gnss.rflink.gps.SubFrame`
    
        Container for sub-frames 2.
    
        Table 20-1, sheet 2 and table 40-1, sheet 2 in
        :class:`~org.orekit.gnss.rflink.gps.https:.navcen.uscg.gov.sites.default.files.pdf.gps.IS`, IS-GPS-200N, 22 Aug 2022
    
        Since:
            12.0
    """
    def getAODO(self) -> int:
        """
            Get Age Of data Offset.
        
            Returns:
                Age Of Data Offset (s)
        
        
        """
        ...
    def getCrs(self) -> float:
        """
            Get Crs.
        
            Returns:
                crs (m)
        
        
        """
        ...
    def getCuc(self) -> float:
        """
            Get Cuc.
        
            Returns:
                Cuc (rad)
        
        
        """
        ...
    def getCus(self) -> float:
        """
            Get Cus.
        
            Returns:
                Cus (rad)
        
        
        """
        ...
    def getDeltaN(self) -> float:
        """
            Get Δn.
        
            Returns:
                Δn (rad/s)
        
        
        """
        ...
    def getE(self) -> float:
        """
            Get e.
        
            Returns:
                e
        
        
        """
        ...
    def getFitInterval(self) -> int:
        """
            Get fit interval.
        
            Returns:
                fit interval
        
        
        """
        ...
    def getIODE(self) -> int:
        """
            Get Issue Of Data (ephemeris).
        
            Returns:
                Issue Of Data (ephemeris)
        
        
        """
        ...
    def getM0(self) -> float:
        """
            Get M₀.
        
            Returns:
                M₀ (rad)
        
        
        """
        ...
    def getSqrtA(self) -> float:
        """
            Get √a.
        
            Returns:
                d√a (√m)
        
        
        """
        ...
    def getToe(self) -> int:
        """
            Get Time Of Ephemeris.
        
            Returns:
                Time Of Ephemeris
        
        
        """
        ...

class SubFrame3(SubFrame):
    """
    public class SubFrame3 extends :class:`~org.orekit.gnss.rflink.gps.SubFrame`
    
        Container for sub-frames 3.
    
        Table 20-1, sheet 3 and table 40-1, sheet 3 in
        :class:`~org.orekit.gnss.rflink.gps.https:.navcen.uscg.gov.sites.default.files.pdf.gps.IS`, IS-GPS-200N, 22 Aug 2022
    
        Since:
            12.0
    """
    def getCic(self) -> float:
        """
            Get Cic.
        
            Returns:
                Cic (rad)
        
        
        """
        ...
    def getCis(self) -> float:
        """
            Get Cis.
        
            Returns:
                Cis (rad)
        
        
        """
        ...
    def getCrc(self) -> float:
        """
            Get Crc.
        
            Returns:
                Crc (rad)
        
        
        """
        ...
    def getI0(self) -> float:
        """
            Get i₀.
        
            Returns:
                i₀ (rad)
        
        
        """
        ...
    def getIDot(self) -> float:
        """
            Get dot(i).
        
            Returns:
                dot(i) (rad/s)
        
        
        """
        ...
    def getIODE(self) -> int:
        """
            Get Issue Of Data (ephemeris).
        
            Returns:
                Issue Of Data (ephemeris)
        
        
        """
        ...
    def getLowercaseOmega(self) -> float:
        """
            Get ω.
        
            Returns:
                ω(rad)
        
        
        """
        ...
    def getOmegaDot(self) -> float:
        """
            Get dot(Ω).
        
            Returns:
                dot(Ω) (rad/s)
        
        
        """
        ...
    def getUppercaseOmega0(self) -> float:
        """
            Get Ω₀.
        
            Returns:
                Ω₀ (rad)
        
        
        """
        ...

class SubFrame45(SubFrame):
    """
    public class SubFrame45 extends :class:`~org.orekit.gnss.rflink.gps.SubFrame`
    
        Base container for sub-frames 4 and 5.
    
        Since:
            12.0
    """
    def getDataId(self) -> int:
        """
            Get data ID.
        
            Returns:
                data ID
        
        
        """
        ...
    def getSvId(self) -> int:
        """
            Get SV (page) ID.
        
            Returns:
                SV (page) ID
        
        
        """
        ...

class SubFrame4A(SubFrame45):
    """
    public class SubFrame4A extends :class:`~org.orekit.gnss.rflink.gps.SubFrame45`
    
        Container for sub-frames 4, pages 1, 6, 11, 16 and 21, but also for sub-frames 4, pages 2, 3, 4, 5, 7, 8, and 9 which
        have a similar structure.
    
        Table 40-1, sheets 6 and 7 in
        :class:`~org.orekit.gnss.rflink.gps.https:.navcen.uscg.gov.sites.default.files.pdf.gps.IS`, IS-GPS-200N, 22 Aug 2022
    
        Since:
            12.0
    """
    def getReserved03(self) -> int:
        """
            Get the reserved field in word 3.
        
            Returns:
                reserved field in word 3
        
        
        """
        ...
    def getReserved04(self) -> int:
        """
            Get the reserved field in word 4.
        
            Returns:
                reserved field in word 4
        
        
        """
        ...
    def getReserved05(self) -> int:
        """
            Get the reserved field in word 5.
        
            Returns:
                reserved field in word 5
        
        
        """
        ...
    def getReserved06(self) -> int:
        """
            Get the reserved field in word 6.
        
            Returns:
                reserved field in word 6
        
        
        """
        ...
    def getReserved07(self) -> int:
        """
            Get the reserved field in word 7.
        
            Returns:
                reserved field in word 7
        
        
        """
        ...
    def getReserved08(self) -> int:
        """
            Get the reserved field in word 8.
        
            Returns:
                reserved field in word 8
        
        
        """
        ...
    def getReserved10(self) -> int:
        """
            Get the reserved field in word 10.
        
            Returns:
                reserved field in word 10
        
        
        """
        ...
    def getReservedA09(self) -> int:
        """
            Get the reserved field A in word 9.
        
            Returns:
                reserved field A in word 9
        
        
        """
        ...
    def getReservedB09(self) -> int:
        """
            Get the reserved field B in word 9.
        
            Returns:
                reserved field B in word 9
        
        
        """
        ...

class SubFrame4B(SubFrame45):
    """
    public class SubFrame4B extends :class:`~org.orekit.gnss.rflink.gps.SubFrame45`
    
        Container for sub-frames 4, pages 10, 14, 15, 17.
    
        Table 40-1, sheet 11 in :class:`~org.orekit.gnss.rflink.gps.https:.navcen.uscg.gov.sites.default.files.pdf.gps.IS`,
        IS-GPS-200N, 22 Aug 2022
    
        Since:
            12.0
    """
    def getReserved03(self) -> int:
        """
            Get the reserved field in word 3.
        
            Returns:
                reserved field in word 3
        
        
        """
        ...
    def getReserved04(self) -> int:
        """
            Get the reserved field in word 4.
        
            Returns:
                reserved field in word 4
        
        
        """
        ...
    def getReserved05(self) -> int:
        """
            Get the reserved field in word 5.
        
            Returns:
                reserved field in word 5
        
        
        """
        ...
    def getReserved06(self) -> int:
        """
            Get the reserved field in word 6.
        
            Returns:
                reserved field in word 6
        
        
        """
        ...
    def getReserved07(self) -> int:
        """
            Get the reserved field in word 7.
        
            Returns:
                reserved field in word 7
        
        
        """
        ...
    def getReserved08(self) -> int:
        """
            Get the reserved field in word 8.
        
            Returns:
                reserved field in word 8
        
        
        """
        ...
    def getReserved09(self) -> int:
        """
            Get the reserved field in word 9.
        
            Returns:
                reserved field in word 9
        
        
        """
        ...
    def getReserved10(self) -> int:
        """
            Get the reserved field in word 10.
        
            Returns:
                reserved field in word 10
        
        
        """
        ...

class SubFrame4C(SubFrame45):
    """
    public class SubFrame4C extends :class:`~org.orekit.gnss.rflink.gps.SubFrame45`
    
        Container for sub-frames 4, page 13.
    
        Table 40-1, sheet 10 in :class:`~org.orekit.gnss.rflink.gps.https:.navcen.uscg.gov.sites.default.files.pdf.gps.IS`,
        IS-GPS-200N, 22 Aug 2022
    
        Since:
            12.0
    """
    NB_ERD: typing.ClassVar[int] = ...
    """
    public static final int NB_ERD
    
        Number of Estimated Range Deviations.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getERD(self, int: int) -> int:
        """
            Get an Estimated Range Deviation.
        
            Parameters:
                index (int): index of the ERD (between 1 and :meth:`~org.orekit.gnss.rflink.gps.SubFrame4C.NB_ERD`)
        
            Returns:
                Estimated Range Deviation
        
        
        """
        ...

class SubFrame4D(SubFrame45):
    """
    public class SubFrame4D extends :class:`~org.orekit.gnss.rflink.gps.SubFrame45`
    
        Container for sub-frames 4, page 18.
    
        Table 40-1, sheet 8 in :class:`~org.orekit.gnss.rflink.gps.https:.navcen.uscg.gov.sites.default.files.pdf.gps.IS`,
        IS-GPS-200N, 22 Aug 2022
    
        Since:
            12.0
    """
    def getA0(self) -> float:
        """
            Get A0 field.
        
            Returns:
                A0 field (seconds).
        
        
        """
        ...
    def getA1(self) -> float:
        """
            Get A₁ field.
        
            Returns:
                A₁ field (second/second).
        
        
        """
        ...
    def getAlpha0(self) -> float:
        """
            Get α₀ field.
        
            Returns:
                α₀ field (second).
        
        
        """
        ...
    def getAlpha1(self) -> float:
        """
            Get α₁ field.
        
            Returns:
                α₁ field (second/rad).
        
        
        """
        ...
    def getAlpha2(self) -> float:
        """
            Get α₂ field.
        
            Returns:
                α₂ field (second/rad²).
        
        
        """
        ...
    def getAlpha3(self) -> float:
        """
            Get α₃ field.
        
            Returns:
                α₃ field (second/rad³)
        
        
        """
        ...
    def getBeta0(self) -> float:
        """
            Get β₀ field.
        
            Returns:
                β₀ field (second)
        
        
        """
        ...
    def getBeta1(self) -> float:
        """
            Get β₁ field.
        
            Returns:
                β₁ field (second/rad)
        
        
        """
        ...
    def getBeta2(self) -> float:
        """
            Get β₂ field.
        
            Returns:
                β₂ field (second/rad²)
        
        
        """
        ...
    def getBeta3(self) -> float:
        """
            Get β₃ field.
        
            Returns:
                β₃ field (second/rad³)
        
        
        """
        ...
    def getDeltaTLs(self) -> int:
        """
            Get ΔtLS field.
        
            Returns:
                ΔtLS field.
        
        
        """
        ...
    def getDeltaTLsf(self) -> int:
        """
            Get ΔtLSF field.
        
            Returns:
                ΔtLSF field.
        
        
        """
        ...
    def getDn(self) -> int:
        """
            Get DN field.
        
            Returns:
                DN field.
        
        
        """
        ...
    def getReserved10(self) -> int:
        """
            Get reserved field in word 10.
        
            Returns:
                reserved field in word 10.
        
        
        """
        ...
    def getTot(self) -> int:
        """
            Get TOT field.
        
            Returns:
                TOT field.
        
        
        """
        ...
    def getWeekNumberLsf(self) -> int:
        """
            Get Week Number LSF field.
        
            Returns:
                Week Number LSF field.
        
        
        """
        ...
    def getWeekNumberT(self) -> int:
        """
            Get Week Number T field.
        
            Returns:
                Week Number T field.
        
        
        """
        ...

class SubFrame4E(SubFrame45):
    """
    public class SubFrame4E extends :class:`~org.orekit.gnss.rflink.gps.SubFrame45`
    
        Container for sub-frames 4, page 25.
    
        Table 20-1, sheet 9 and table 40-1, sheet 9 in
        :class:`~org.orekit.gnss.rflink.gps.https:.navcen.uscg.gov.sites.default.files.pdf.gps.IS`, IS-GPS-200N, 22 Aug 2022
    
        Since:
            12.0
    """
    NB_AS: typing.ClassVar[int] = ...
    """
    public static final int NB_AS
    
        Number of Anti-spoofing entries.
    
        Also see:
            :meth:`~constant`
    
    
    """
    NB_SVH: typing.ClassVar[int] = ...
    """
    public static final int NB_SVH
    
        Number of SV health entries.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def getAntiSpoofing(self) -> int: ...
    @typing.overload
    def getAntiSpoofing(self, int: int) -> int:
        """
            Get the anti-spoofing for a satellite.
        
            Parameters:
                index (int): in the sub-frame (from 1 to 32, beware it is not the satellite number, it is also related to
                    :meth:`~org.orekit.gnss.rflink.gps.SubFrame45.getDataId`)
        
            Returns:
                anti-spoofing
        
        
        """
        ...
    def getReserved10(self) -> int:
        """
            Get the reserved field in word 10.
        
            Returns:
                reserved field in word 10
        
        
        """
        ...
    def getReserved8(self) -> int:
        """
            Get the reserved field in word 8.
        
            Returns:
                reserved field in word 8
        
        
        """
        ...
    def getSvHealth(self, int: int) -> int:
        """
            Get the Sv health for a satellite.
        
            Parameters:
                index (int): in the sub-frame (from 1 to 7 or 1 to 8 depending on :meth:`~org.orekit.gnss.rflink.gps.SubFrame45.getDataId`, beware it
                    is not the satellite number, it is also related to :meth:`~org.orekit.gnss.rflink.gps.SubFrame45.getDataId`), an
        
            Returns:
                anti-spoofing
        
        
        """
        ...

class SubFrame5B(SubFrame45):
    """
    public class SubFrame5B extends :class:`~org.orekit.gnss.rflink.gps.SubFrame45`
    
        Container for sub-frames 5, page 25.
    
        Table 20-1, sheet 5 and table 40-1, sheet 5 in
        :class:`~org.orekit.gnss.rflink.gps.https:.navcen.uscg.gov.sites.default.files.pdf.gps.IS`, IS-GPS-200N, 22 Aug 2022
    
        Since:
            12.0
    """
    def getReservedA10(self) -> int:
        """
            Get the reserved field A in word 10.
        
            Returns:
                reserved field A in word 10
        
        
        """
        ...
    def getReservedB10(self) -> int:
        """
            Get the reserved field B in word 10.
        
            Returns:
                reserved field B in word 10
        
        
        """
        ...
    def getSvHealth(self, int: int) -> int:
        """
            Get the SV Health for a satellite.
        
            Parameters:
                index (int): in the sub-frame (from 1 to 24, beware it is not the satellite number, it is also related to
                    :meth:`~org.orekit.gnss.rflink.gps.SubFrame45.getDataId`)
        
            Returns:
                SV health
        
        
        """
        ...
    def getTOA(self) -> int:
        """
            Get Time of Almanac.
        
            Returns:
                time of almanac (seconds)
        
        
        """
        ...
    def getWeekNumber(self) -> int:
        """
            Get the almanac week number.
        
            Returns:
                almanac week number
        
        
        """
        ...

class SubFrameAlmanac(SubFrame45):
    """
    public class SubFrameAlmanac extends :class:`~org.orekit.gnss.rflink.gps.SubFrame45`
    
        Container for sub-frames 5, page 1-24.
    
        Table 20-1, sheet 4 and table 40-1, sheet 4 in
        :class:`~org.orekit.gnss.rflink.gps.https:.navcen.uscg.gov.sites.default.files.pdf.gps.IS`, IS-GPS-200N, 22 Aug 2022
    
        Since:
            12.0
    """
    def getAF0(self) -> float:
        """
            Get af₀.
        
            Returns:
                af₀ (second)
        
        
        """
        ...
    def getAF1(self) -> float:
        """
            Get af₁.
        
            Returns:
                af₁ (second/second)
        
        
        """
        ...
    def getDeltai(self) -> float:
        """
            Get Δi.
        
            Returns:
                Δi (rad)
        
        
        """
        ...
    def getE(self) -> float:
        """
            Get eccentricity.
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getLowercaseOmega(self) -> float:
        """
            Get ω.
        
            Returns:
                ω(rad)
        
        
        """
        ...
    def getM0(self) -> float:
        """
            Get M₀.
        
            Returns:
                M₀ (rad)
        
        
        """
        ...
    def getOmegaDot(self) -> float:
        """
            Get dot(Ω).
        
            Returns:
                dot(Ω) (rad/s)
        
        
        """
        ...
    def getPRN(self) -> int:
        """
            Get the PRN code phase of the SV.
        
            Returns:
                PRN code phase
        
        
        """
        ...
    def getSqrtA(self) -> float:
        """
            Get √a.
        
            Returns:
                d√a (√m)
        
        
        """
        ...
    def getSvHealth(self) -> int:
        """
            Get SV health.
        
            Returns:
                SV health
        
        
        """
        ...
    def getToaA(self) -> int:
        """
            Get Time Of Almanac.
        
            Returns:
                Time Of Almanac (seconds)
        
        
        """
        ...
    def getUppercaseOmega0(self) -> float:
        """
            Get Ω₀.
        
            Returns:
                Ω₀ (rad)
        
        
        """
        ...

class SubFrameDummyAlmanac(SubFrame45):
    """
    public class SubFrameDummyAlmanac extends :class:`~org.orekit.gnss.rflink.gps.SubFrame45`
    
        Almanac for dummy SV.
    
        Section 20.3.3.5.1.2 Almanac Data in
        :class:`~org.orekit.gnss.rflink.gps.https:.navcen.uscg.gov.sites.default.files.pdf.gps.IS`, IS-GPS-200N, 22 Aug 2022
    
        Since:
            12.0
    """
    ...

class SubFrame4A0(SubFrame4A):
    """
    public class SubFrame4A0 extends :class:`~org.orekit.gnss.rflink.gps.SubFrame4A`
    
        Container for sub-frames 4, pages 1, 6, 11, 16 and 21.
    
        Table 40-1, sheet 6 in :class:`~org.orekit.gnss.rflink.gps.https:.navcen.uscg.gov.sites.default.files.pdf.gps.IS`,
        IS-GPS-200N, 22 Aug 2022
    
        Since:
            12.0
    """
    ...

class SubFrame4A1(SubFrame4A):
    """
    public class SubFrame4A1 extends :class:`~org.orekit.gnss.rflink.gps.SubFrame4A`
    
        Container for sub-frames 4, pages 2, 3, 4, 5, 7, 8, and 9.
    
        Table 40-1, sheet 7 in :class:`~org.orekit.gnss.rflink.gps.https:.navcen.uscg.gov.sites.default.files.pdf.gps.IS`,
        IS-GPS-200N, 22 Aug 2022
    
        Since:
            12.0
    """
    ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.rflink.gps")``.

    SubFrame: typing.Type[SubFrame]
    SubFrame1: typing.Type[SubFrame1]
    SubFrame2: typing.Type[SubFrame2]
    SubFrame3: typing.Type[SubFrame3]
    SubFrame45: typing.Type[SubFrame45]
    SubFrame4A: typing.Type[SubFrame4A]
    SubFrame4A0: typing.Type[SubFrame4A0]
    SubFrame4A1: typing.Type[SubFrame4A1]
    SubFrame4B: typing.Type[SubFrame4B]
    SubFrame4C: typing.Type[SubFrame4C]
    SubFrame4D: typing.Type[SubFrame4D]
    SubFrame4E: typing.Type[SubFrame4E]
    SubFrame5B: typing.Type[SubFrame5B]
    SubFrameAlmanac: typing.Type[SubFrameAlmanac]
    SubFrameDummyAlmanac: typing.Type[SubFrameDummyAlmanac]
