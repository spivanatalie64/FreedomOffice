package org.freedomoffice.canvas;

import org.freedomoffice.FreedomOfficeMainActivity;

import org.freedomoffice.R;

/**
 * Selection handle for showing and manipulating the end of a selection.
 */
public class SelectionHandleEnd extends SelectionHandle {
    public SelectionHandleEnd(FreedomOfficeMainActivity context) {
        super(context, getBitmapForDrawable(context, R.drawable.handle_alias_end));
    }

    /**
     * Define the type of the handle.
     */
    @Override
    public HandleType getHandleType() {
        return HandleType.END;
    }
}
