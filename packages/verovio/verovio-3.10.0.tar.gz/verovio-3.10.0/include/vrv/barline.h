/////////////////////////////////////////////////////////////////////////////
// Name:        barline.h
// Author:      Laurent Pugin
// Created:     2011
// Copyright (c) Authors and others. All rights reserved.
/////////////////////////////////////////////////////////////////////////////

#ifndef __VRV_BARLINE_H__
#define __VRV_BARLINE_H__

#include "atts_shared.h"
#include "layerelement.h"

namespace vrv {

enum class BarLinePosition { None, Left, Right };

//----------------------------------------------------------------------------
// BarLine
//----------------------------------------------------------------------------

/**
 * This class models the MEI <barLine> element.
 */
class BarLine : public LayerElement,
                public AttBarLineLog,
                public AttColor,
                public AttNNumberLike,
                public AttVisibility {
public:
    /**
     * @name Constructors, destructors, and other standard methods
     * Reset method resets all attribute classes.
     */
    ///@{
    BarLine();
    BarLine(ClassId classId);
    virtual ~BarLine();
    Object *Clone() const override { return new BarLine(*this); }
    void Reset() override;
    std::string GetClassName() const override { return "BarLine"; }
    ///@}

    /** Override the method since alignment is required */
    bool HasToBeAligned() const override { return true; }

    /**
     * Use to set the alignment for the Measure BarLine members.
     * This is as special case where we need to add to the measure aligner.
     */
    bool SetAlignment(Alignment *alignment);

    /*
     * Return true if the barLine type requires repetition dots to be drawn.
     */
    bool HasRepetitionDots() const;

    /**
     * @name Get and set the position
     */
    BarLinePosition GetPosition() const { return m_position; }
    void SetPosition(BarLinePosition position) { m_position = position; }

    //----------//
    // Functors //
    //----------//

    /**
     * See Object::ConvertToCastOffMensural
     */
    int ConvertToCastOffMensural(FunctorParams *functorParams) override;

private:
    //
public:
    //
private:
    /** The barline position (left/right) */
    BarLinePosition m_position;
};

} // namespace vrv

#endif
