/* -*- Mode: C; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- */
/*
 * This file is part of the FreedomOffice project.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

#ifndef INCLUDED_FREEDOMOFFICEKIT_FREEDOMOFFICEKIT_H
#define INCLUDED_FREEDOMOFFICEKIT_FREEDOMOFFICEKIT_H

#include <stddef.h>

// the unstable API needs C99's bool
// TODO remove the C99 types from the API before making stable
#if defined LOK_USE_UNSTABLE_API || defined LIBO_INTERNAL_ONLY
# ifndef _WIN32
#  include <stdbool.h>
# endif
# include <stdint.h>
#endif

#ifdef __APPLE__
#include <TargetConditionals.h>
#endif

#include "FreedomOfficeKitTypes.h"

#ifdef __cplusplus
extern "C"
{
#endif

typedef struct FreedomOfficeKitStruct FreedomOfficeKit;
typedef struct FreedomOfficeKitClassStruct FreedomOfficeKitClass;

typedef struct FreedomOfficeKitDocumentStruct FreedomOfficeKitDocument;
typedef struct FreedomOfficeKitDocumentClassStruct FreedomOfficeKitDocumentClass;

// Do we have an extended member in this struct ?
#define FREEDOMOFFICEKIT_HAS_MEMBER(strct,member,nSize) \
    (offsetof(strct, member) < (nSize))

#define FREEDOMOFFICEKIT_HAS(pKit,member) FREEDOMOFFICEKIT_HAS_MEMBER(FreedomOfficeKitClass,member,(pKit)->pClass->nSize)

struct FreedomOfficeKitStruct
{
    FreedomOfficeKitClass* pClass;
};

struct FreedomOfficeKitClassStruct
{
    size_t  nSize;

    void (*destroy) (FreedomOfficeKit* pThis);

    FreedomOfficeKitDocument* (*documentLoad) (FreedomOfficeKit* pThis,
                                             const char* pURL);

    char* (*getError) (FreedomOfficeKit* pThis);

    /// @since FreedomOffice 5.0
    FreedomOfficeKitDocument* (*documentLoadWithOptions) (FreedomOfficeKit* pThis,
                                                        const char* pURL,
                                                        const char* pOptions);
    /// @since FreedomOffice 5.2

    /// The name "freeError" is a historical accident, actually this
    /// is a generic deallocation function for dynamically allocated
    /// memory returned by other FreedomOfficeKit functions.

    /// Especially on Windows it is important to not call free() in
    /// your own code on a pointer returned from some random other
    /// dynamic library (like the one this code goes into) where it
    /// might have been allocated by calling malloc() (etc) in a C
    /// runtime library that is different from the one used by your
    /// code. That will lead to a crash. Always call the free() in the
    /// same C runtime where the malloc() that allocated the pointer
    /// is.

    void (*freeError) (char* pFree);

    /// @since FreedomOffice 6.0
    void (*registerCallback) (FreedomOfficeKit* pThis,
                              FreedomOfficeKitCallback pCallback,
                              void* pData);

    /** @see lok::Office::getFilterTypes().
        @since FreedomOffice 6.0
     */
    char* (*getFilterTypes) (FreedomOfficeKit* pThis);

    /** @see lok::Office::setOptionalFeatures().
        @since FreedomOffice 6.0
     */
    void (*setOptionalFeatures)(FreedomOfficeKit* pThis, unsigned long long features);

    /** @see lok::Office::setDocumentPassword().
        @since FreedomOffice 6.0
     */
    void (*setDocumentPassword) (FreedomOfficeKit* pThis,
            char const* pURL,
            char const* pPassword);

    /** @see lok::Office::getVersionInfo().
        @since FreedomOffice 6.0
     */
    char* (*getVersionInfo) (FreedomOfficeKit* pThis);

    /** @see lok::Office::runMacro().
        @since FreedomOffice 6.0
     */
    int (*runMacro) (FreedomOfficeKit *pThis, const char* pURL);

    /** @see lok::Office::signDocument().
        @since FreedomOffice 6.2
     */
     bool (*signDocument) (FreedomOfficeKit* pThis,
                           const char* pUrl,
                           const unsigned char* pCertificateBinary,
                           const int nCertificateBinarySize,
                           const unsigned char* pPrivateKeyBinary,
                           const int nPrivateKeyBinarySize);

    /// @see lok::Office::runLoop()
    void (*runLoop) (FreedomOfficeKit* pThis,
                     FreedomOfficeKitPollCallback pPollCallback,
                     FreedomOfficeKitWakeCallback pWakeCallback,
                     void* pData);

    /// @see lok::Office::setOption
    void (*setOption) (FreedomOfficeKit* pThis, const char* pOption, const char* pValue);

    /// @see lok::Office::dumpState
    /// @since FreedomOffice 7.5
    void (*dumpState) (FreedomOfficeKit* pThis, const char* pOptions, char** pState);

    /** @see lok::Office::extractRequest.
     */
    char* (*extractRequest) (FreedomOfficeKit* pThis,
                           const char* pFilePath);

    /// @see lok::Office::trimMemory
    /// @since FreedomOffice 7.6
    void (*trimMemory) (FreedomOfficeKit* pThis, int nTarget);

    /// @see lok::Office::startURP
    void* (*startURP)(FreedomOfficeKit* pThis,
                    void* pReceiveURPFromLOContext, void* pSendURPToLOContext,
                    int (*fnReceiveURPFromLO)(void* pContext, const signed char* pBuffer, int nLen),
                    int (*fnSendURPToLO)(void* pContext, signed char* pBuffer, int nLen));

    /// @see lok::Office::stopURP
    void (*stopURP)(FreedomOfficeKit* pThis, void* pSendURPToLOContext);

    /// @see lok::Office::joinThreads
    int (*joinThreads)(FreedomOfficeKit* pThis);

    /// @see lok::Office::startThreads
    void (*startThreads)(FreedomOfficeKit* pThis);

    /// @see lok::Office::setForkedChild
    void (*setForkedChild)(FreedomOfficeKit* pThis, bool bIsChild);

    /** @see lok::Office::extractDocumentStructureRequest.
     */
    char* (*extractDocumentStructureRequest)(FreedomOfficeKit* pThis, const char* pFilePath,
                                             const char* pFilter);

    /// @see lok::Office::registerAnyInputCallback()
    void (*registerAnyInputCallback)(FreedomOfficeKit* pThis,
                                     FreedomOfficeKitAnyInputCallback pCallback, void* pData);

    /// @see lok::Office::getDocsCount().
    int (*getDocsCount) (FreedomOfficeKit* pThis);

    /// @see lok::Office::registerFileSaveDialogCallback()
    void (*registerFileSaveDialogCallback)(FreedomOfficeKit* pThis,
            FreedomOfficeKitFileSaveDialogCallback pCallback);
};

#define FREEDOMOFFICEKIT_DOCUMENT_HAS(pDoc,member) FREEDOMOFFICEKIT_HAS_MEMBER(FreedomOfficeKitDocumentClass,member,(pDoc)->pClass->nSize)

struct FreedomOfficeKitDocumentStruct
{
    FreedomOfficeKitDocumentClass* pClass;
};

struct FreedomOfficeKitDocumentClassStruct
{
    size_t  nSize;

    void (*destroy) (FreedomOfficeKitDocument* pThis);

    int (*saveAs) (FreedomOfficeKitDocument* pThis,
                   const char* pUrl,
                   const char* pFormat,
                   const char* pFilterOptions);

    /** @see lok::Document::getDocumentType().
        @since FreedomOffice 6.0
     */
    int (*getDocumentType) (FreedomOfficeKitDocument* pThis);

#if defined LOK_USE_UNSTABLE_API || defined LIBO_INTERNAL_ONLY
    /// @see lok::Document::getParts().
    int (*getParts) (FreedomOfficeKitDocument* pThis);

    /// @see lok::Document::getPartPageRectangles().
    char* (*getPartPageRectangles) (FreedomOfficeKitDocument* pThis);

    /// @see lok::Document::getPart().
    int (*getPart) (FreedomOfficeKitDocument* pThis);

    /// @see lok::Document::setPart().
    void (*setPart) (FreedomOfficeKitDocument* pThis,
                     int nPart);

    /// @see lok::Document::getPartName().
    char* (*getPartName) (FreedomOfficeKitDocument* pThis,
                          int nPart);

    /// @see lok::Document::setPartMode().
    void (*setPartMode) (FreedomOfficeKitDocument* pThis,
                         int nMode);

    /// @see lok::Document::paintTile().
    void (*paintTile) (FreedomOfficeKitDocument* pThis,
                       unsigned char* pBuffer,
                       const int nCanvasWidth,
                       const int nCanvasHeight,
                       const int nTilePosX,
                       const int nTilePosY,
                       const int nTileWidth,
                       const int nTileHeight);

    /// @see lok::Document::getTileMode().
    int (*getTileMode) (FreedomOfficeKitDocument* pThis);

    /// @see lok::Document::getDocumentSize().
    void (*getDocumentSize) (FreedomOfficeKitDocument* pThis,
                             long* pWidth,
                             long* pHeight);

    /// @see lok::Document::initializeForRendering().
    void (*initializeForRendering) (FreedomOfficeKitDocument* pThis,
                                    const char* pArguments);

    /// @see lok::Document::registerCallback().
    void (*registerCallback) (FreedomOfficeKitDocument* pThis,
                              FreedomOfficeKitCallback pCallback,
                              void* pData);

    /// @see lok::Document::postKeyEvent
    void (*postKeyEvent) (FreedomOfficeKitDocument* pThis,
                          int nType,
                          int nCharCode,
                          int nKeyCode);

    /// @see lok::Document::postMouseEvent
    void (*postMouseEvent) (FreedomOfficeKitDocument* pThis,
                            int nType,
                            int nX,
                            int nY,
                            int nCount,
                            int nButtons,
                            int nModifier);

    /// @see lok::Document::postUnoCommand
    void (*postUnoCommand) (FreedomOfficeKitDocument* pThis,
                            const char* pCommand,
                            const char* pArguments,
                            bool bNotifyWhenFinished);

    /// @see lok::Document::setTextSelection
    void (*setTextSelection) (FreedomOfficeKitDocument* pThis,
                              int nType,
                              int nX,
                              int nY);

    /// @see lok::Document::getTextSelection
    char* (*getTextSelection) (FreedomOfficeKitDocument* pThis,
                               const char* pMimeType,
                               char** pUsedMimeType);

    /// @see lok::Document::paste().
    bool (*paste) (FreedomOfficeKitDocument* pThis,
                   const char* pMimeType,
                   const char* pData,
                   size_t nSize);

    /// @see lok::Document::setGraphicSelection
    void (*setGraphicSelection) (FreedomOfficeKitDocument* pThis,
                                 int nType,
                                 int nX,
                                 int nY);

    /// @see lok::Document::resetSelection
    void (*resetSelection) (FreedomOfficeKitDocument* pThis);

    /// @see lok::Document::getCommandValues().
    char* (*getCommandValues) (FreedomOfficeKitDocument* pThis, const char* pCommand);

    /// @see lok::Document::setClientZoom().
    void (*setClientZoom) (FreedomOfficeKitDocument* pThis,
            int nTilePixelWidth,
            int nTilePixelHeight,
            int nTileTwipWidth,
            int nTileTwipHeight);

    /// @see lok::Document::setVisibleArea).
    void (*setClientVisibleArea) (FreedomOfficeKitDocument* pThis, int nX, int nY, int nWidth, int nHeight);

    /// @see lok::Document::createView().
    int (*createView) (FreedomOfficeKitDocument* pThis);
    /// @see lok::Document::destroyView().
    void (*destroyView) (FreedomOfficeKitDocument* pThis, int nId);
    /// @see lok::Document::setView().
    void (*setView) (FreedomOfficeKitDocument* pThis, int nId);
    /// @see lok::Document::getView().
    int (*getView) (FreedomOfficeKitDocument* pThis);
    /// @see lok::Document::getViewsCount().
    int (*getViewsCount) (FreedomOfficeKitDocument* pThis);

    /// @see lok::Document::renderFont().
    unsigned char* (*renderFont) (FreedomOfficeKitDocument* pThis,
                       const char* pFontName,
                       const char* pChar,
                       int* pFontWidth,
                       int* pFontHeight);

    /// @see lok::Document::getPartHash().
    char* (*getPartHash) (FreedomOfficeKitDocument* pThis,
                          int nPart);

    /// Paints a tile from a specific part.
    /// @see lok::Document::paintTile().
    void (*paintPartTile) (FreedomOfficeKitDocument* pThis,
                           unsigned char* pBuffer,
                           const int nPart,
                           const int nMode,
                           const int nCanvasWidth,
                           const int nCanvasHeight,
                           const int nTilePosX,
                           const int nTilePosY,
                           const int nTileWidth,
                           const int nTileHeight);

    /// @see lok::Document::getViewIds().
    bool (*getViewIds) (FreedomOfficeKitDocument* pThis,
                       int* pArray,
                       size_t nSize);

    /// @see lok::Document::setOutlineState).
    void (*setOutlineState) (FreedomOfficeKitDocument* pThis, bool bColumn, int nLevel, int nIndex, bool bHidden);

    /// Paints window with given id to the buffer
    /// @see lok::Document::paintWindow().
    void (*paintWindow) (FreedomOfficeKitDocument* pThis, unsigned nWindowId,
                         unsigned char* pBuffer,
                         const int x, const int y,
                         const int width, const int height);

    /// @see lok::Document::postWindow().
    void (*postWindow) (FreedomOfficeKitDocument* pThis, unsigned nWindowId, int nAction, const char* pData);

    /// @see lok::Document::postWindowKeyEvent().
    void (*postWindowKeyEvent) (FreedomOfficeKitDocument* pThis,
                                unsigned nWindowId,
                                int nType,
                                int nCharCode,
                                int nKeyCode);

    /// @see lok::Document::postWindowMouseEvent().
    void (*postWindowMouseEvent) (FreedomOfficeKitDocument* pThis,
                                  unsigned nWindowId,
                                  int nType,
                                  int nX,
                                  int nY,
                                  int nCount,
                                  int nButtons,
                                  int nModifier);

    /// @see lok::Document::setViewLanguage().
    void (*setViewLanguage) (FreedomOfficeKitDocument* pThis, int nId, const char* language);

    /// @see lok::Document::postWindowExtTextInputEvent
    void (*postWindowExtTextInputEvent) (FreedomOfficeKitDocument* pThis,
                                         unsigned nWindowId,
                                         int nType,
                                         const char* pText);

    /// @see lok::Document::getPartInfo().
    char* (*getPartInfo) (FreedomOfficeKitDocument* pThis, int nPart);

    /// Paints window with given id to the buffer with the give DPI scale
    /// (every pixel is dpiscale-times larger).
    /// @see lok::Document::paintWindow().
    void (*paintWindowDPI) (FreedomOfficeKitDocument* pThis, unsigned nWindowId,
                            unsigned char* pBuffer,
                            const int x, const int y,
                            const int width, const int height,
                            const double dpiscale);

// CERTIFICATE AND SIGNING

    /// @see lok::Document::insertCertificate().
    bool (*insertCertificate) (FreedomOfficeKitDocument* pThis,
                                const unsigned char* pCertificateBinary,
                                const int nCertificateBinarySize,
                                const unsigned char* pPrivateKeyBinary,
                                const int nPrivateKeyBinarySize);

    /// @see lok::Document::addCertificate().
    bool (*addCertificate) (FreedomOfficeKitDocument* pThis,
                                const unsigned char* pCertificateBinary,
                                const int nCertificateBinarySize);

    /// @see lok::Document::getSignatureState().
    int (*getSignatureState) (FreedomOfficeKitDocument* pThis);
// END CERTIFICATE AND SIGNING

    /// @see lok::Document::renderShapeSelection
    size_t (*renderShapeSelection)(FreedomOfficeKitDocument* pThis, char** pOutput);

    /// @see lok::Document::postWindowGestureEvent().
    void (*postWindowGestureEvent) (FreedomOfficeKitDocument* pThis,
                                  unsigned nWindowId,
                                  const char* pType,
                                  int nX,
                                  int nY,
                                  int nOffset);

    /// @see lok::Document::createViewWithOptions().
    int (*createViewWithOptions) (FreedomOfficeKitDocument* pThis, const char* pOptions);

    /// @see lok::Document::selectPart().
    void (*selectPart) (FreedomOfficeKitDocument* pThis, int nPart, int nSelect);

    /// @see lok::Document::moveSelectedParts().
    void (*moveSelectedParts) (FreedomOfficeKitDocument* pThis, int nPosition, bool bDuplicate);

    /// Resize window with given id.
    /// @see lok::Document::resizeWindow().
    void (*resizeWindow) (FreedomOfficeKitDocument* pThis, unsigned nWindowId,
                          const int width, const int height);

    /// Pass a nullptr terminated array of mime-type strings
    /// @see lok::Document::getClipboard for more details
    int (*getClipboard) (FreedomOfficeKitDocument* pThis,
                         const char **pMimeTypes,
                         size_t      *pOutCount,
                         char      ***pOutMimeTypes,
                         size_t     **pOutSizes,
                         char      ***pOutStreams);

    /// @see lok::Document::setClipboard
    int (*setClipboard) (FreedomOfficeKitDocument* pThis,
                         const size_t   nInCount,
                         const char   **pInMimeTypes,
                         const size_t  *pInSizes,
                         const char   **pInStreams);

    /// @see lok::Document::getSelectionType
    int (*getSelectionType) (FreedomOfficeKitDocument* pThis);

    /// @see lok::Document::removeTextContext
    void (*removeTextContext) (FreedomOfficeKitDocument* pThis,
                               unsigned nWindowId,
                               int nBefore,
                               int nAfter);

    /// @see lok::Document::renderFontOrientation().
    unsigned char* (*renderFontOrientation) (FreedomOfficeKitDocument* pThis,
                       const char* pFontName,
                       const char* pChar,
                       int* pFontWidth,
                       int* pFontHeight,
                       int pOrientation);

    /// Switches view to viewId if viewId >= 0, and paints window
    /// @see lok::Document::paintWindowDPI().
    void (*paintWindowForView) (FreedomOfficeKitDocument* pThis, unsigned nWindowId,
                                unsigned char* pBuffer,
                                const int x, const int y,
                                const int width, const int height,
                                const double dpiscale,
                                int viewId);

    /// @see lok::Document::completeFunction().
    void (*completeFunction) (FreedomOfficeKitDocument* pThis, const char* pFunctionName);

    /// @see lok::Document::setWindowTextSelection
    void (*setWindowTextSelection) (FreedomOfficeKitDocument* pThis,
                                    unsigned nWindowId,
                                    bool bSwap,
                                    int nX,
                                    int nY);

    /// @see lok::Document::sendFormFieldEvent
    void (*sendFormFieldEvent) (FreedomOfficeKitDocument* pThis,
                                const char* pArguments);

    /// @see lok::Document::setBlockedCommandList
    void (*setBlockedCommandList) (FreedomOfficeKitDocument* pThis,
                                int nViewId,
                                const char* blockedCommandList);

    /// @see lok::Document::renderSearchResult
    bool (*renderSearchResult) (FreedomOfficeKitDocument* pThis,
                                const char* pSearchResult,
                                unsigned char** pBitmapBuffer,
                                int* pWidth, int* pHeight, size_t* pByteSize);

    /// @see lok::Document::sendContentControlEvent().
    void (*sendContentControlEvent)(FreedomOfficeKitDocument* pThis, const char* pArguments);

    /// @see lok::Document::getSelectionTypeAndText
    /// @since FreedomOffice 7.4
    int (*getSelectionTypeAndText) (FreedomOfficeKitDocument* pThis,
                                    const char* pMimeType,
                                    char** pText,
                                    char** pUsedMimeType);

    /// @see lok::Document::getDataArea().
    void (*getDataArea) (FreedomOfficeKitDocument* pThis,
                         long nPart,
                         long* pCol,
                         long* pRow);

    /// @see lok::Document::getEditMode().
    int (*getEditMode) (FreedomOfficeKitDocument* pThis);

    /// @see lok::Document::setViewTimezone().
    void (*setViewTimezone) (FreedomOfficeKitDocument* pThis, int nId, const char* timezone);

    /// @see lok::Document::setAccessibilityState().
    void (*setAccessibilityState) (FreedomOfficeKitDocument* pThis, int nId, bool nEnabled);

    /// @see lok::Document::getA11yFocusedParagraph.
    char* (*getA11yFocusedParagraph) (FreedomOfficeKitDocument* pThis);

    /// @see lok::Document::getA11yCaretPosition.
    int (*getA11yCaretPosition) (FreedomOfficeKitDocument* pThis);

    /// @see lok::Document::setViewReadOnly().
    void (*setViewReadOnly) (FreedomOfficeKitDocument* pThis, int nId, const bool readOnly);

    /// @see lok::Document::getPresentationInfo
    char* (*getPresentationInfo) (FreedomOfficeKitDocument* pThis);

    /// @see lok::Document::createSlideRenderer
    bool (*createSlideRenderer) (
        FreedomOfficeKitDocument* pThis,
        const char* pSlideHash,
        int nSlideNumber, unsigned* nViewWidth, unsigned* nViewHeight,
        bool bRenderBackground, bool bRenderMasterPage);

    /// @see lok::Document::postSlideshowCleanup
    void (*postSlideshowCleanup)(FreedomOfficeKitDocument* pThis);

    /// @see lok::Document::renderNextSlideLayer
    bool (*renderNextSlideLayer)(
        FreedomOfficeKitDocument* pThis, unsigned char* pBuffer, bool* bIsBitmapLayer, double* pScale, char** pJsonMessage);

    /// @see lok::Document::setViewOption
    void (*setViewOption)(FreedomOfficeKitDocument* pThis, const char* pOption, const char* pValue);

    /// @see lok::Document::setColorPreviewState().
    void (*setColorPreviewState) (FreedomOfficeKitDocument* pThis, int nId, bool nEnabled);

#endif // defined LOK_USE_UNSTABLE_API || defined LIBO_INTERNAL_ONLY
};

#ifdef __cplusplus
}
#endif

#endif // INCLUDED_FREEDOMOFFICEKIT_FREEDOMOFFICEKIT_H

/* vim:set shiftwidth=4 softtabstop=4 expandtab: */
