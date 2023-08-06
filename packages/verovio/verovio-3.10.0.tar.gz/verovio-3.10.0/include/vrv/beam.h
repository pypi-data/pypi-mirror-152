/////////////////////////////////////////////////////////////////////////////
// Name:        beam.h
// Author:      Rodolfo Zitellini
// Created:     26/06/2012
// Copyright (c) Authors and others. All rights reserved.
/////////////////////////////////////////////////////////////////////////////

#ifndef __VRV_BEAM_H__
#define __VRV_BEAM_H__

#include "atts_cmn.h"
#include "atts_shared.h"
#include "drawinginterface.h"
#include "layerelement.h"

namespace vrv {

class BeamElementCoord;
class TabDurSym;
class StaffAlignment;

// the maximum allowed number of partials
#define MAX_DURATION_PARTIALS 16

enum { PARTIAL_NONE = 0, PARTIAL_THROUGH, PARTIAL_RIGHT, PARTIAL_LEFT };

//----------------------------------------------------------------------------
// BeamSegment
//----------------------------------------------------------------------------

/**
 * Class for storing drawing parameters when calculating beams.
 * See View::DrawBeam and View::CalcBeam
 */

class BeamSegment {
public:
    /**
     * @name Constructors, destructors, and other standard methods
     */
    ///@{
    BeamSegment();
    virtual ~BeamSegment();

    void Reset();

    void CalcBeam(Layer *layer, Staff *staff, Doc *doc, BeamDrawingInterface *beamInterface,
        data_BEAMPLACE place = BEAMPLACE_NONE, bool init = true);

    /**
     *
     */
    const ArrayOfBeamElementCoords *GetElementCoordRefs() const;

    /**
     * Initializes the m_beamElementCoords vector objects.
     * This is called by Beam::FilterList
     */
    void InitCoordRefs(const ArrayOfBeamElementCoords *beamElementCoords);

    /**
     * Clear the m_beamElementCoords vector and delete all the objects.
     */
    void ClearCoordRefs();

    /**
     * Get longest duration of the elements that are adjacent to the X coordinate passed
     */
    int GetAdjacentElementsDuration(int elementX) const;

    /**
     * @name Getters for the X and Y starting value of the beam;
     */
    ///@{
    int GetStartingX() const;
    int GetStartingY() const;
    ///@}

    /**
     * @name Getters for the stem same as role.
     */
    ///@{
    bool StemSameas() const { return (m_stemSameasRole != SAMEAS_NONE); }
    bool StemSameasIsUnset() const { return (m_stemSameasRole == SAMEAS_UNSET); }
    bool StemSameasIsPrimary() const { return (m_stemSameasRole == SAMEAS_PRIMARY); }
    bool StemSameasIsSecondary() const { return (m_stemSameasRole == SAMEAS_SECONDARY); }
    ///@}

    /**
     * @name Methods to intialize and update the role for stem.sameas context
     * Before the drawing beam place has been calculated, the role is marked as unset.
     * Then it is marked as primary or secondary depending on the beam place.
     */
    ///@{
    void InitSameasRoles(Beam *sameasBeam, data_BEAMPLACE &drawingPlace);
    void UpdateSameasRoles(data_BEAMPLACE place);
    void CalcNoteHeadShiftForStemSameas(Doc *doc, Beam *sameasBeam, data_BEAMPLACE place);
    ///@}

private:
    // Helper to adjust stem length to extend only towards outmost subbeam (if option "--beam-french-style" is set)
    void AdjustBeamToFrenchStyle(BeamDrawingInterface *beamInterface);

    // Helper to adjust beam positioning with regards to ledger lines (top and bottom of the staff)
    void AdjustBeamToLedgerLines(Doc *doc, Staff *staff, BeamDrawingInterface *beamInterface, bool isHorizontal);

    /**
     * Helper to calculate required adjustment to beam position and stem length for beams that have tremolos or notes
     * with stem modifiers
     */
    void AdjustBeamToTremolos(Doc *doc, Staff *staff, BeamDrawingInterface *beamInterface);

    void CalcBeamInit(Staff *staff, Doc *doc, BeamDrawingInterface *beamInterface, data_BEAMPLACE place);

    void CalcBeamInitForNotePair(Note *note1, Note *note2, Staff *staff, int &yMax, int &yMin);

    bool CalcBeamSlope(Staff *staff, Doc *doc, BeamDrawingInterface *beamInterface, int &step);

    int CalcBeamSlopeStep(Doc *doc, Staff *staff, BeamDrawingInterface *beamInterface, int noteStep, bool &shortStep);

    void CalcMixedBeamStem(BeamDrawingInterface *beamInterface, int step);

    void CalcBeamPosition(Doc *doc, Staff *staff, BeamDrawingInterface *beamInterface, bool isHorizontal);

    void CalcAdjustSlope(Staff *staff, Doc *doc, BeamDrawingInterface *beamInterface, int &step);

    // Helper to adjust position of starting point to make sure that beam start-/endpoints touch the staff lines
    void CalcAdjustPosition(Staff *staff, Doc *doc, BeamDrawingInterface *beamInterface);

    void CalcBeamPlace(Layer *layer, BeamDrawingInterface *beamInterface, data_BEAMPLACE place);

    /**
     * Helper to calculate the beam position for a beam in tablature.
     * Also adjust the drawingYRel of the TabDurSym if necessary.
     */
    void CalcBeamPlaceTab(
        Layer *layer, Staff *staff, Doc *doc, BeamDrawingInterface *beamInterface, data_BEAMPLACE place);

    // Helper to calculate the longest stem length of the beam (which will be used uniformely)
    void CalcBeamStemLength(Staff *staff, data_BEAMPLACE place, bool isHorizontal);

    // Helper to set the stem values
    void CalcSetStemValues(Staff *staff, Doc *doc, BeamDrawingInterface *beamInterface);

    // Helper to set the stem values for tablature
    void CalcSetStemValuesTab(Staff *staff, Doc *doc, BeamDrawingInterface *beamInterface);

    // Helper to calculate max/min beam points for the relative beam place
    std::pair<int, int> CalcBeamRelativeMinMax(data_BEAMPLACE place) const;

    // Helper to calculate location and duration of the note that would be setting highest/lowest point for the beam
    std::pair<int, int> CalcStemDefiningNote(Staff *staff, data_BEAMPLACE place);

    // Calculate positioning for the horizontal beams
    void CalcHorizontalBeam(Doc *doc, Staff *staff, BeamDrawingInterface *beamInterface);

    // Helper to calculate relative position of the beam to for each of the coordinates
    void CalcMixedBeamPlace(Staff *staff);

    // Helper to calculate proper positioning of the additional beamlines for notes
    void CalcPartialFlagPlace();

    // Helper to simply set the values of each BeamElementCoord according the the first position and the slope
    void CalcSetValues();

    // Helper to check wheter beam fits within certain bounds
    bool DoesBeamOverlap(int staffTop, int topOffset, int staffBottom, int bottomOffset, bool isCrossStaff = false);

    // Helper to check mixed beam positioning compared to other elements (ledger lines, staff) and adjust it accordingly
    bool NeedToResetPosition(Staff *staff, Doc *doc, BeamDrawingInterface *beamInterface);

public:
    // values set by CalcBeam
    int m_nbNotesOrChords;
    double m_beamSlope; // the slope of the beam
    int m_verticalCenter;
    int m_ledgerLinesAbove;
    int m_ledgerLinesBelow;
    int m_uniformStemLength;
    data_BEAMPLACE m_weightedPlace;

    BeamElementCoord *m_firstNoteOrChord;
    BeamElementCoord *m_lastNoteOrChord;

    /**
     * An array of coordinates for each element
     **/
    ArrayOfBeamElementCoords m_beamElementCoordRefs;

    /**
     * @name The role in a stem.sameas situation.
     * Set in BeamSegment::InitSameasRoles and then in UpdateSameasRoles
     * Used to determine if the beam is the primary one (normal stems and beams)
     * or the secondary one (linking both notes). This depends on the drawing beam place,
     * which can be encoded but otherwise calculated by CalcBeamPlace.
     * The pointer to the other beam m_stemSameasReverseRole is set only for the first of the
     * two beams and is not bi-directional. Is is set in InitSameasRoles.
     */
    ///@{
    StemSameasDrawingRole m_stemSameasRole;
    StemSameasDrawingRole *m_stemSameasReverseRole;
    ///@}
};

//----------------------------------------------------------------------------
// BeamSpanSegment
//----------------------------------------------------------------------------

// Class for storing additional information regarding beamSegment placement (in case of beamSpan spanning over
// the systems)
class BeamSpanSegment : public BeamSegment {
public:
    BeamSpanSegment();
    virtual ~BeamSpanSegment(){};

    /**
     * Set/get methods for member variables
     */
    ///@{
    Measure *GetMeasure() const { return m_measure; }
    void SetMeasure(Measure *measure) { m_measure = measure; }
    Staff *GetStaff() const { return m_staff; }
    void SetStaff(Staff *staff) { m_staff = staff; }
    Layer *GetLayer() const { return m_layer; }
    void SetLayer(Layer *layer) { m_layer = layer; }
    BeamElementCoord *GetBeginCoord() const { return m_begin; }
    void SetBeginCoord(BeamElementCoord *begin) { m_begin = begin; }
    BeamElementCoord *GetEndCoord() const { return m_end; }
    void SetEndCoord(BeamElementCoord *end) { m_end = end; }
    ///@}

    /**
     * Set/get methods for spanning type of segment.
     * Set spanning type based on the positioning of the beam segment
     */
    ///@{
    void SetSpanningType(int systemIndex, int systemCount);
    int GetSpanningType() const { return m_spanningType; }
    ///@}

    // Helper to append coordinates for the beamSpans that are drawn over systems
    void AppendSpanningCoordinates(Measure *measure);

private:
    // main values to track positioning of the segment
    Measure *m_measure;
    Staff *m_staff;
    Layer *m_layer;
    BeamElementCoord *m_begin;
    BeamElementCoord *m_end;

    // spanning type for purposes of adding additional coordinates to segment
    int m_spanningType = SPANNING_START_END;
};

//----------------------------------------------------------------------------
// Beam
//----------------------------------------------------------------------------

class Beam : public LayerElement,
             public BeamDrawingInterface,
             public AttBeamedWith,
             public AttBeamRend,
             public AttColor,
             public AttCue {
public:
    /**
     * @name Constructors, destructors, and other standard methods
     * Reset method resets all attribute classes.
     */
    ///@{
    Beam();
    virtual ~Beam();
    Object *Clone() const override { return new Beam(*this); }
    void Reset() override;
    std::string GetClassName() const override { return "Beam"; }
    ///@}

    /**
     * @name Getter to interfaces
     */
    ///@{
    BeamDrawingInterface *GetBeamDrawingInterface() override { return vrv_cast<BeamDrawingInterface *>(this); }
    const BeamDrawingInterface *GetBeamDrawingInterface() const override
    {
        return vrv_cast<const BeamDrawingInterface *>(this);
    }
    ///@}

    int GetNoteCount() const { return this->GetChildCount(NOTE); }

    /**
     * Add an element (a note or a rest) to a beam.
     * Only Note or Rest elements will be actually added to the beam.
     */
    bool IsSupportedChild(Object *object) override;

    /**
     *
     */
    const ArrayOfBeamElementCoords *GetElementCoords();

    /**

     * Return true if the beam has a tabGrp child.
     * In that case, the ObjectList will only have tabGrp elements. See Beam::FilterList
     */
    bool IsTabBeam() const;

    /**
     * @name Checker, getter and setter for a beam with which the stems are shared
     */
    ///@{
    bool HasStemSameasBeam() const { return (m_stemSameas); }
    Beam *GetStemSameasBeam() const { return m_stemSameas; }
    void SetStemSameasBeam(Beam *stemSameas) { m_stemSameas = stemSameas; }
    ///@}

    /**
     * See DrawingInterface::GetAdditionalBeamCount
     */
    std::pair<int, int> GetAdditionalBeamCount() const override;

    /**
     * Return duration of beam part that are closest to the specified object X position
     */
    int GetBeamPartDuration(Object *object) const;

    //----------//
    // Functors //
    //----------//

    /**
     * See Object::AdjustBeams
     */
    int AdjustBeams(FunctorParams *functorParams) override;

    /**
     * See Object::AdjustBeamsEnd
     */
    int AdjustBeamsEnd(FunctorParams *functorParams) override;

    /**
     * See Object::CalcStem
     */
    int CalcStem(FunctorParams *functorParams) override;

    /**
     * See Object::ResetHorizontalAlignment
     */
    int ResetHorizontalAlignment(FunctorParams *functorParams) override;

    /**
     * See Object::ResetData
     */
    int ResetData(FunctorParams *functorParams) override;

protected:
    /**
     * Filter the flat list and keep only Note and Chords elements.
     * This also initializes the m_beamElementCoords vector
     */
    void FilterList(ListOfConstObjects &childList) const override;

    /**
     * See LayerElement::SetElementShortening
     */
    void SetElementShortening(int shortening) override;

    /**
     * Return duration of beam part for specified X coordinate. Duration of two closest elements is taken for this
     * purpose.
     */
    int GetBeamPartDuration(int x) const;

private:
    /**
     * A pointer to the beam with which stems are shared.
     * The pointer is bi-directional – each beam points to the other one.
     * It is set in Note::ResovleStemSameas()
     */
    Beam *m_stemSameas;

public:
    /** */
    BeamSegment m_beamSegment;
};

//----------------------------------------------------------------------------
// BeamElementCoord
//----------------------------------------------------------------------------

class BeamElementCoord {
public:
    /**
     * @name Constructors, destructors, and other standard methods
     */
    ///@{
    BeamElementCoord()
    {
        m_element = NULL;
        m_closestNote = NULL;
        m_tabDurSym = NULL;
        m_stem = NULL;
        m_overlapMargin = 0;
        m_maxShortening = -1;
        m_beamRelativePlace = BEAMPLACE_NONE;
        m_partialFlagPlace = BEAMPLACE_NONE;
    }
    virtual ~BeamElementCoord();

    /**
     * Return the encoded stem direction.
     * Access the value in the Stem element if already set.
     */
    data_STEMDIRECTION GetStemDir() const;

    void SetDrawingStemDir(
        data_STEMDIRECTION stemDir, Staff *staff, Doc *doc, BeamSegment *segment, BeamDrawingInterface *interface);

    /** Set the note or closest note for chord or tabdursym for tablature beams placed outside the staff */
    void SetClosestNoteOrTabDurSym(data_STEMDIRECTION stemDir, bool outsideStaff);

    /** Heleper for calculating the stem length for staff notation and tablature beams within the staff */
    int CalculateStemLength(Staff *staff, data_STEMDIRECTION stemDir, bool isHorizontal);

    /** Helper for calculating the stem length for tablature beam placed outside the staff */
    int CalculateStemLengthTab(Staff *staff, data_STEMDIRECTION stemDir);

    /**
     * Return stem length adjustment in half units, depending on the @stem.mode attribute
     */
    int CalculateStemModAdjustment(int stemLength, int directionBias);

    /**
     * Helper to get the StemmedDrawingInterface associated with the m_element (if any)
     * Return the Chord or Note interface if the element if of that type.
     * Return the TabDurSym interface if the element is TabDurGrp and has a TabDurSym descendant.
     * Return NULL otherwise.
     */
    StemmedDrawingInterface *GetStemHolderInterface();

    int m_x;
    int m_yBeam; // y value of stem top position
    int m_dur; // drawing duration
    int m_breaksec;
    int m_overlapMargin;
    int m_maxShortening; // maximum allowed shortening in half units
    bool m_centered; // beam is centered on the line
    data_BEAMPLACE m_beamRelativePlace;
    char m_partialFlags[MAX_DURATION_PARTIALS];
    data_BEAMPLACE m_partialFlagPlace;
    LayerElement *m_element;
    Note *m_closestNote;
    TabDurSym *m_tabDurSym;
    Stem *m_stem; // a pointer to the stem in order to avoid to have to re-cast it
};

} // namespace vrv

#endif
