const char * SDL_GetPlatform (void);
typedef int8_t Sint8;
typedef uint8_t Uint8;
typedef int16_t Sint16;
typedef uint16_t Uint16;
typedef int32_t Sint32;
typedef uint32_t Uint32;
typedef int64_t Sint64;
typedef uint64_t Uint64;
void * SDL_malloc(size_t size);
void * SDL_calloc(size_t nmemb, size_t size);
void * SDL_realloc(void *mem, size_t size);
void SDL_free(void *mem);
char * SDL_getenv(const char *name);
int SDL_setenv(const char *name, const char *value, int overwrite);
void SDL_qsort(void *base, size_t nmemb, size_t size, int (*compare) (const void *, const void *));
int SDL_abs(int x);
int SDL_isdigit(int x);
int SDL_isspace(int x);
int SDL_toupper(int x);
int SDL_tolower(int x);
void * SDL_memset( void *dst, int c, size_t len);
void * SDL_memcpy( void *dst, const void *src, size_t len);
void * SDL_memmove( void *dst, const void *src, size_t len);
int SDL_memcmp(const void *s1, const void *s2, size_t len);
size_t SDL_wcslen(const wchar_t *wstr);
size_t SDL_wcslcpy( wchar_t *dst, const wchar_t *src, size_t maxlen);
size_t SDL_wcslcat( wchar_t *dst, const wchar_t *src, size_t maxlen);
size_t SDL_strlen(const char *str);
size_t SDL_strlcpy( char *dst, const char *src, size_t maxlen);
size_t SDL_utf8strlcpy( char *dst, const char *src, size_t dst_bytes);
size_t SDL_strlcat( char *dst, const char *src, size_t maxlen);
char * SDL_strdup(const char *str);
char * SDL_strrev(char *str);
char * SDL_strupr(char *str);
char * SDL_strlwr(char *str);
char * SDL_strchr(const char *str, int c);
char * SDL_strrchr(const char *str, int c);
char * SDL_strstr(const char *haystack, const char *needle);
char * SDL_itoa(int value, char *str, int radix);
char * SDL_uitoa(unsigned int value, char *str, int radix);
char * SDL_ltoa(long value, char *str, int radix);
char * SDL_ultoa(unsigned long value, char *str, int radix);
char * SDL_lltoa(Sint64 value, char *str, int radix);
char * SDL_ulltoa(Uint64 value, char *str, int radix);
int SDL_atoi(const char *str);
double SDL_atof(const char *str);
long SDL_strtol(const char *str, char **endp, int base);
unsigned long SDL_strtoul(const char *str, char **endp, int base);
Sint64 SDL_strtoll(const char *str, char **endp, int base);
Uint64 SDL_strtoull(const char *str, char **endp, int base);
double SDL_strtod(const char *str, char **endp);
int SDL_strcmp(const char *str1, const char *str2);
int SDL_strncmp(const char *str1, const char *str2, size_t maxlen);
int SDL_strcasecmp(const char *str1, const char *str2);
int SDL_strncasecmp(const char *str1, const char *str2, size_t len);
double SDL_acos(double x);
double SDL_asin(double x);
double SDL_atan(double x);
double SDL_atan2(double x, double y);
double SDL_ceil(double x);
double SDL_copysign(double x, double y);
double SDL_cos(double x);
float SDL_cosf(float x);
double SDL_fabs(double x);
double SDL_floor(double x);
double SDL_log(double x);
double SDL_pow(double x, double y);
double SDL_scalbn(double x, int n);
double SDL_sin(double x);
float SDL_sinf(float x);
double SDL_sqrt(double x);
float SDL_sqrtf(float x);
double SDL_tan(double x);
float SDL_tanf(float x);
typedef struct _SDL_iconv_t *SDL_iconv_t;
SDL_iconv_t SDL_iconv_open(const char *tocode,
                                                   const char *fromcode);
int SDL_iconv_close(SDL_iconv_t cd);
size_t SDL_iconv(SDL_iconv_t cd, const char **inbuf,
                                         size_t * inbytesleft, char **outbuf,
                                         size_t * outbytesleft);
char * SDL_iconv_string(const char *tocode,
                                               const char *fromcode,
                                               const char *inbuf,
                                               size_t inbytesleft);
void SDL_SetMainReady(void);
typedef struct SDL_AssertData
{
    int always_ignore;
    unsigned int trigger_count;
    const char *condition;
    const char *filename;
    int linenum;
    const char *function;
    const struct SDL_AssertData *next;
} SDL_AssertData;
SDL_AssertState SDL_ReportAssertion(SDL_AssertData *,
                                                             const char *,
                                                             const char *, int)
;
typedef SDL_AssertState ( *SDL_AssertionHandler)(
                                 const SDL_AssertData* data, void* userdata);
void SDL_SetAssertionHandler(
                                            SDL_AssertionHandler handler,
                                            void *userdata);
SDL_AssertionHandler SDL_GetDefaultAssertionHandler(void);
SDL_AssertionHandler SDL_GetAssertionHandler(void **puserdata);
const SDL_AssertData * SDL_GetAssertionReport(void);
void SDL_ResetAssertionReport(void);
typedef int SDL_SpinLock;
SDL_bool SDL_AtomicTryLock(SDL_SpinLock *lock);
void SDL_AtomicLock(SDL_SpinLock *lock);
void SDL_AtomicUnlock(SDL_SpinLock *lock);
typedef struct { int value; } SDL_atomic_t;
SDL_bool SDL_AtomicCAS(SDL_atomic_t *a, int oldval, int newval);
int SDL_AtomicSet(SDL_atomic_t *a, int v);
int SDL_AtomicGet(SDL_atomic_t *a);
int SDL_AtomicAdd(SDL_atomic_t *a, int v);
SDL_bool SDL_AtomicCASPtr(void **a, void *oldval, void *newval);
void* SDL_AtomicSetPtr(void **a, void* v);
void* SDL_AtomicGetPtr(void **a);
int SDL_SetError( const char *fmt, ...);
const char * SDL_GetError(void);
void SDL_ClearError(void);
int SDL_Error(SDL_errorcode code);
struct SDL_mutex;
typedef struct SDL_mutex SDL_mutex;
SDL_mutex * SDL_CreateMutex(void);
int SDL_LockMutex(SDL_mutex * mutex);
int SDL_TryLockMutex(SDL_mutex * mutex);
int SDL_UnlockMutex(SDL_mutex * mutex);
void SDL_DestroyMutex(SDL_mutex * mutex);
struct SDL_semaphore;
typedef struct SDL_semaphore SDL_sem;
SDL_sem * SDL_CreateSemaphore(Uint32 initial_value);
void SDL_DestroySemaphore(SDL_sem * sem);
int SDL_SemWait(SDL_sem * sem);
int SDL_SemTryWait(SDL_sem * sem);
int SDL_SemWaitTimeout(SDL_sem * sem, Uint32 ms);
int SDL_SemPost(SDL_sem * sem);
Uint32 SDL_SemValue(SDL_sem * sem);
struct SDL_cond;
typedef struct SDL_cond SDL_cond;
SDL_cond * SDL_CreateCond(void);
void SDL_DestroyCond(SDL_cond * cond);
int SDL_CondSignal(SDL_cond * cond);
int SDL_CondBroadcast(SDL_cond * cond);
int SDL_CondWait(SDL_cond * cond, SDL_mutex * mutex);
int SDL_CondWaitTimeout(SDL_cond * cond,
                                                SDL_mutex * mutex, Uint32 ms);
struct SDL_Thread;
typedef struct SDL_Thread SDL_Thread;
typedef unsigned long SDL_threadID;
typedef unsigned int SDL_TLSID;
typedef int ( * SDL_ThreadFunction) (void *data);
SDL_Thread *
SDL_CreateThread(SDL_ThreadFunction fn, const char *name, void *data);
const char * SDL_GetThreadName(SDL_Thread *thread);
SDL_threadID SDL_ThreadID(void);
SDL_threadID SDL_GetThreadID(SDL_Thread * thread);
int SDL_SetThreadPriority(SDL_ThreadPriority priority);
void SDL_WaitThread(SDL_Thread * thread, int *status);
void SDL_DetachThread(SDL_Thread * thread);
SDL_TLSID SDL_TLSCreate(void);
void * SDL_TLSGet(SDL_TLSID id);
int SDL_TLSSet(SDL_TLSID id, const void *value, void (*destructor)(void*));
typedef struct SDL_RWops
{
    Sint64 ( * size) (struct SDL_RWops * context);
    Sint64 ( * seek) (struct SDL_RWops * context, Sint64 offset,
                             int whence);
    size_t ( * read) (struct SDL_RWops * context, void *ptr,
                             size_t size, size_t maxnum);
    size_t ( * write) (struct SDL_RWops * context, const void *ptr,
                              size_t size, size_t num);
    int ( * close) (struct SDL_RWops * context);
    Uint32 type;
    union
    {
        struct
        {
            SDL_bool autoclose;
            FILE *fp;
        } stdio;
        struct
        {
            Uint8 *base;
            Uint8 *here;
            Uint8 *stop;
        } mem;
        struct
        {
            void *data1;
            void *data2;
        } unknown;
    } hidden;
} SDL_RWops;
SDL_RWops * SDL_RWFromFile(const char *file,
                                                  const char *mode);
SDL_RWops * SDL_RWFromFP(FILE * fp,
                                                SDL_bool autoclose);
SDL_RWops * SDL_RWFromMem(void *mem, int size);
SDL_RWops * SDL_RWFromConstMem(const void *mem,
                                                      int size);
SDL_RWops * SDL_AllocRW(void);
void SDL_FreeRW(SDL_RWops * area);
Uint8 SDL_ReadU8(SDL_RWops * src);
Uint16 SDL_ReadLE16(SDL_RWops * src);
Uint16 SDL_ReadBE16(SDL_RWops * src);
Uint32 SDL_ReadLE32(SDL_RWops * src);
Uint32 SDL_ReadBE32(SDL_RWops * src);
Uint64 SDL_ReadLE64(SDL_RWops * src);
Uint64 SDL_ReadBE64(SDL_RWops * src);
size_t SDL_WriteU8(SDL_RWops * dst, Uint8 value);
size_t SDL_WriteLE16(SDL_RWops * dst, Uint16 value);
size_t SDL_WriteBE16(SDL_RWops * dst, Uint16 value);
size_t SDL_WriteLE32(SDL_RWops * dst, Uint32 value);
size_t SDL_WriteBE32(SDL_RWops * dst, Uint32 value);
size_t SDL_WriteLE64(SDL_RWops * dst, Uint64 value);
size_t SDL_WriteBE64(SDL_RWops * dst, Uint64 value);
typedef Uint16 SDL_AudioFormat;
typedef void ( * SDL_AudioCallback) (void *userdata, Uint8 * stream,
                                            int len);
typedef struct SDL_AudioSpec
{
    int freq;
    SDL_AudioFormat format;
    Uint8 channels;
    Uint8 silence;
    Uint16 samples;
    Uint16 padding;
    Uint32 size;
    SDL_AudioCallback callback;
    void *userdata;
} SDL_AudioSpec;
struct SDL_AudioCVT;
typedef void ( * SDL_AudioFilter) (struct SDL_AudioCVT * cvt,
                                          SDL_AudioFormat format);
typedef struct SDL_AudioCVT
{
    int needed;
    SDL_AudioFormat src_format;
    SDL_AudioFormat dst_format;
    double rate_incr;
    Uint8 *buf;
    int len;
    int len_cvt;
    int len_mult;
    double len_ratio;
    SDL_AudioFilter filters[10];
    int filter_index;
} SDL_AudioCVT;
int SDL_GetNumAudioDrivers(void);
const char * SDL_GetAudioDriver(int index);
int SDL_AudioInit(const char *driver_name);
void SDL_AudioQuit(void);
const char * SDL_GetCurrentAudioDriver(void);
int SDL_OpenAudio(SDL_AudioSpec * desired,
                                          SDL_AudioSpec * obtained);
typedef Uint32 SDL_AudioDeviceID;
int SDL_GetNumAudioDevices(int iscapture);
const char * SDL_GetAudioDeviceName(int index,
                                                           int iscapture);
SDL_AudioDeviceID SDL_OpenAudioDevice(const char
                                                              *device,
                                                              int iscapture,
                                                              const
                                                              SDL_AudioSpec *
                                                              desired,
                                                              SDL_AudioSpec *
                                                              obtained,
                                                              int
                                                              allowed_changes);
SDL_AudioStatus SDL_GetAudioStatus(void);
SDL_AudioStatus
SDL_GetAudioDeviceStatus(SDL_AudioDeviceID dev);
void SDL_PauseAudio(int pause_on);
void SDL_PauseAudioDevice(SDL_AudioDeviceID dev,
                                                  int pause_on);
SDL_AudioSpec * SDL_LoadWAV_RW(SDL_RWops * src,
                                                      int freesrc,
                                                      SDL_AudioSpec * spec,
                                                      Uint8 ** audio_buf,
                                                      Uint32 * audio_len);
void SDL_FreeWAV(Uint8 * audio_buf);
int SDL_BuildAudioCVT(SDL_AudioCVT * cvt,
                                              SDL_AudioFormat src_format,
                                              Uint8 src_channels,
                                              int src_rate,
                                              SDL_AudioFormat dst_format,
                                              Uint8 dst_channels,
                                              int dst_rate);
int SDL_ConvertAudio(SDL_AudioCVT * cvt);
void SDL_MixAudio(Uint8 * dst, const Uint8 * src,
                                          Uint32 len, int volume);
void SDL_MixAudioFormat(Uint8 * dst,
                                                const Uint8 * src,
                                                SDL_AudioFormat format,
                                                Uint32 len, int volume);
int SDL_QueueAudio(SDL_AudioDeviceID dev, const void *data, Uint32 len);
Uint32 SDL_GetQueuedAudioSize(SDL_AudioDeviceID dev);
void SDL_ClearQueuedAudio(SDL_AudioDeviceID dev);
void SDL_LockAudio(void);
void SDL_LockAudioDevice(SDL_AudioDeviceID dev);
void SDL_UnlockAudio(void);
void SDL_UnlockAudioDevice(SDL_AudioDeviceID dev);
void SDL_CloseAudio(void);
void SDL_CloseAudioDevice(SDL_AudioDeviceID dev);
int SDL_SetClipboardText(const char *text);
char * SDL_GetClipboardText(void);
SDL_bool SDL_HasClipboardText(void);
int SDL_GetCPUCount(void);
int SDL_GetCPUCacheLineSize(void);
SDL_bool SDL_HasRDTSC(void);
SDL_bool SDL_HasAltiVec(void);
SDL_bool SDL_HasMMX(void);
SDL_bool SDL_Has3DNow(void);
SDL_bool SDL_HasSSE(void);
SDL_bool SDL_HasSSE2(void);
SDL_bool SDL_HasSSE3(void);
SDL_bool SDL_HasSSE41(void);
SDL_bool SDL_HasSSE42(void);
SDL_bool SDL_HasAVX(void);
SDL_bool SDL_HasAVX2(void);
int SDL_GetSystemRAM(void);
typedef struct SDL_Color
{
    Uint8 r;
    Uint8 g;
    Uint8 b;
    Uint8 a;
} SDL_Color;
typedef struct SDL_Palette
{
    int ncolors;
    SDL_Color *colors;
    Uint32 version;
    int refcount;
} SDL_Palette;
typedef struct SDL_PixelFormat
{
    Uint32 format;
    SDL_Palette *palette;
    Uint8 BitsPerPixel;
    Uint8 BytesPerPixel;
    Uint8 padding[2];
    Uint32 Rmask;
    Uint32 Gmask;
    Uint32 Bmask;
    Uint32 Amask;
    Uint8 Rloss;
    Uint8 Gloss;
    Uint8 Bloss;
    Uint8 Aloss;
    Uint8 Rshift;
    Uint8 Gshift;
    Uint8 Bshift;
    Uint8 Ashift;
    int refcount;
    struct SDL_PixelFormat *next;
} SDL_PixelFormat;
const char* SDL_GetPixelFormatName(Uint32 format);
SDL_bool SDL_PixelFormatEnumToMasks(Uint32 format,
                                                            int *bpp,
                                                            Uint32 * Rmask,
                                                            Uint32 * Gmask,
                                                            Uint32 * Bmask,
                                                            Uint32 * Amask);
Uint32 SDL_MasksToPixelFormatEnum(int bpp,
                                                          Uint32 Rmask,
                                                          Uint32 Gmask,
                                                          Uint32 Bmask,
                                                          Uint32 Amask);
SDL_PixelFormat * SDL_AllocFormat(Uint32 pixel_format);
void SDL_FreeFormat(SDL_PixelFormat *format);
SDL_Palette * SDL_AllocPalette(int ncolors);
int SDL_SetPixelFormatPalette(SDL_PixelFormat * format,
                                                      SDL_Palette *palette);
int SDL_SetPaletteColors(SDL_Palette * palette,
                                                 const SDL_Color * colors,
                                                 int firstcolor, int ncolors);
void SDL_FreePalette(SDL_Palette * palette);
Uint32 SDL_MapRGB(const SDL_PixelFormat * format,
                                          Uint8 r, Uint8 g, Uint8 b);
Uint32 SDL_MapRGBA(const SDL_PixelFormat * format,
                                           Uint8 r, Uint8 g, Uint8 b,
                                           Uint8 a);
void SDL_GetRGB(Uint32 pixel,
                                        const SDL_PixelFormat * format,
                                        Uint8 * r, Uint8 * g, Uint8 * b);
void SDL_GetRGBA(Uint32 pixel,
                                         const SDL_PixelFormat * format,
                                         Uint8 * r, Uint8 * g, Uint8 * b,
                                         Uint8 * a);
void SDL_CalculateGammaRamp(float gamma, Uint16 * ramp);
typedef struct SDL_Point
{
    int x;
    int y;
} SDL_Point;
typedef struct SDL_Rect
{
    int x, y;
    int w, h;
} SDL_Rect;
SDL_bool SDL_HasIntersection(const SDL_Rect * A,
                                                     const SDL_Rect * B);
SDL_bool SDL_IntersectRect(const SDL_Rect * A,
                                                   const SDL_Rect * B,
                                                   SDL_Rect * result);
void SDL_UnionRect(const SDL_Rect * A,
                                           const SDL_Rect * B,
                                           SDL_Rect * result);
SDL_bool SDL_EnclosePoints(const SDL_Point * points,
                                                   int count,
                                                   const SDL_Rect * clip,
                                                   SDL_Rect * result);
SDL_bool SDL_IntersectRectAndLine(const SDL_Rect *
                                                          rect, int *X1,
                                                          int *Y1, int *X2,
                                                          int *Y2);
typedef struct SDL_Surface
{
    Uint32 flags;
    SDL_PixelFormat *format;
    int w, h;
    int pitch;
    void *pixels;
    void *userdata;
    int locked;
    void *lock_data;
    SDL_Rect clip_rect;
    struct SDL_BlitMap *map;
    int refcount;
} SDL_Surface;
typedef int (*SDL_blit) (struct SDL_Surface * src, SDL_Rect * srcrect,
                         struct SDL_Surface * dst, SDL_Rect * dstrect);
SDL_Surface * SDL_CreateRGBSurface
    (Uint32 flags, int width, int height, int depth,
     Uint32 Rmask, Uint32 Gmask, Uint32 Bmask, Uint32 Amask);
SDL_Surface * SDL_CreateRGBSurfaceFrom(void *pixels,
                                                              int width,
                                                              int height,
                                                              int depth,
                                                              int pitch,
                                                              Uint32 Rmask,
                                                              Uint32 Gmask,
                                                              Uint32 Bmask,
                                                              Uint32 Amask);
void SDL_FreeSurface(SDL_Surface * surface);
int SDL_SetSurfacePalette(SDL_Surface * surface,
                                                  SDL_Palette * palette);
int SDL_LockSurface(SDL_Surface * surface);
void SDL_UnlockSurface(SDL_Surface * surface);
SDL_Surface * SDL_LoadBMP_RW(SDL_RWops * src,
                                                    int freesrc);
int SDL_SaveBMP_RW
    (SDL_Surface * surface, SDL_RWops * dst, int freedst);
int SDL_SetSurfaceRLE(SDL_Surface * surface,
                                              int flag);
int SDL_SetColorKey(SDL_Surface * surface,
                                            int flag, Uint32 key);
int SDL_GetColorKey(SDL_Surface * surface,
                                            Uint32 * key);
int SDL_SetSurfaceColorMod(SDL_Surface * surface,
                                                   Uint8 r, Uint8 g, Uint8 b);
int SDL_GetSurfaceColorMod(SDL_Surface * surface,
                                                   Uint8 * r, Uint8 * g,
                                                   Uint8 * b);
int SDL_SetSurfaceAlphaMod(SDL_Surface * surface,
                                                   Uint8 alpha);
int SDL_GetSurfaceAlphaMod(SDL_Surface * surface,
                                                   Uint8 * alpha);
int SDL_SetSurfaceBlendMode(SDL_Surface * surface,
                                                    SDL_BlendMode blendMode);
int SDL_GetSurfaceBlendMode(SDL_Surface * surface,
                                                    SDL_BlendMode *blendMode);
SDL_bool SDL_SetClipRect(SDL_Surface * surface,
                                                 const SDL_Rect * rect);
void SDL_GetClipRect(SDL_Surface * surface,
                                             SDL_Rect * rect);
SDL_Surface * SDL_ConvertSurface
    (SDL_Surface * src, const SDL_PixelFormat * fmt, Uint32 flags);
SDL_Surface * SDL_ConvertSurfaceFormat
    (SDL_Surface * src, Uint32 pixel_format, Uint32 flags);
int SDL_ConvertPixels(int width, int height,
                                              Uint32 src_format,
                                              const void * src, int src_pitch,
                                              Uint32 dst_format,
                                              void * dst, int dst_pitch);
int SDL_FillRect
    (SDL_Surface * dst, const SDL_Rect * rect, Uint32 color);
int SDL_FillRects
    (SDL_Surface * dst, const SDL_Rect * rects, int count, Uint32 color);
int SDL_UpperBlit
    (SDL_Surface * src, const SDL_Rect * srcrect,
     SDL_Surface * dst, SDL_Rect * dstrect);
int SDL_LowerBlit
    (SDL_Surface * src, SDL_Rect * srcrect,
     SDL_Surface * dst, SDL_Rect * dstrect);
int SDL_SoftStretch(SDL_Surface * src,
                                            const SDL_Rect * srcrect,
                                            SDL_Surface * dst,
                                            const SDL_Rect * dstrect);
int SDL_UpperBlitScaled
    (SDL_Surface * src, const SDL_Rect * srcrect,
    SDL_Surface * dst, SDL_Rect * dstrect);
int SDL_LowerBlitScaled
    (SDL_Surface * src, SDL_Rect * srcrect,
    SDL_Surface * dst, SDL_Rect * dstrect);
typedef struct
{
    Uint32 format;
    int w;
    int h;
    int refresh_rate;
    void *driverdata;
} SDL_DisplayMode;
typedef struct SDL_Window SDL_Window;
typedef void *SDL_GLContext;
int SDL_GetNumVideoDrivers(void);
const char * SDL_GetVideoDriver(int index);
int SDL_VideoInit(const char *driver_name);
void SDL_VideoQuit(void);
const char * SDL_GetCurrentVideoDriver(void);
int SDL_GetNumVideoDisplays(void);
const char * SDL_GetDisplayName(int displayIndex);
int SDL_GetDisplayBounds(int displayIndex, SDL_Rect * rect);
int SDL_GetDisplayDPI(int displayIndex, float * ddpi, float * hdpi, float * vdpi);
int SDL_GetNumDisplayModes(int displayIndex);
int SDL_GetDisplayMode(int displayIndex, int modeIndex,
                                               SDL_DisplayMode * mode);
int SDL_GetDesktopDisplayMode(int displayIndex, SDL_DisplayMode * mode);
int SDL_GetCurrentDisplayMode(int displayIndex, SDL_DisplayMode * mode);
SDL_DisplayMode * SDL_GetClosestDisplayMode(int displayIndex, const SDL_DisplayMode * mode, SDL_DisplayMode * closest);
int SDL_GetWindowDisplayIndex(SDL_Window * window);
int SDL_SetWindowDisplayMode(SDL_Window * window,
                                                     const SDL_DisplayMode
                                                         * mode);
int SDL_GetWindowDisplayMode(SDL_Window * window,
                                                     SDL_DisplayMode * mode);
Uint32 SDL_GetWindowPixelFormat(SDL_Window * window);
SDL_Window * SDL_CreateWindow(const char *title,
                                                      int x, int y, int w,
                                                      int h, Uint32 flags);
SDL_Window * SDL_CreateWindowFrom(const void *data);
Uint32 SDL_GetWindowID(SDL_Window * window);
SDL_Window * SDL_GetWindowFromID(Uint32 id);
Uint32 SDL_GetWindowFlags(SDL_Window * window);
void SDL_SetWindowTitle(SDL_Window * window,
                                                const char *title);
const char * SDL_GetWindowTitle(SDL_Window * window);
void SDL_SetWindowIcon(SDL_Window * window,
                                               SDL_Surface * icon);
void* SDL_SetWindowData(SDL_Window * window,
                                                const char *name,
                                                void *userdata);
void * SDL_GetWindowData(SDL_Window * window,
                                                const char *name);
void SDL_SetWindowPosition(SDL_Window * window,
                                                   int x, int y);
void SDL_GetWindowPosition(SDL_Window * window,
                                                   int *x, int *y);
void SDL_SetWindowSize(SDL_Window * window, int w,
                                               int h);
void SDL_GetWindowSize(SDL_Window * window, int *w,
                                               int *h);
void SDL_SetWindowMinimumSize(SDL_Window * window,
                                                      int min_w, int min_h);
void SDL_GetWindowMinimumSize(SDL_Window * window,
                                                      int *w, int *h);
void SDL_SetWindowMaximumSize(SDL_Window * window,
                                                      int max_w, int max_h);
void SDL_GetWindowMaximumSize(SDL_Window * window,
                                                      int *w, int *h);
void SDL_SetWindowBordered(SDL_Window * window,
                                                   SDL_bool bordered);
void SDL_ShowWindow(SDL_Window * window);
void SDL_HideWindow(SDL_Window * window);
void SDL_RaiseWindow(SDL_Window * window);
void SDL_MaximizeWindow(SDL_Window * window);
void SDL_MinimizeWindow(SDL_Window * window);
void SDL_RestoreWindow(SDL_Window * window);
int SDL_SetWindowFullscreen(SDL_Window * window,
                                                    Uint32 flags);
SDL_Surface * SDL_GetWindowSurface(SDL_Window * window);
int SDL_UpdateWindowSurface(SDL_Window * window);
int SDL_UpdateWindowSurfaceRects(SDL_Window * window,
                                                         const SDL_Rect * rects,
                                                         int numrects);
void SDL_SetWindowGrab(SDL_Window * window,
                                               SDL_bool grabbed);
SDL_bool SDL_GetWindowGrab(SDL_Window * window);
SDL_Window * SDL_GetGrabbedWindow(void);
int SDL_SetWindowBrightness(SDL_Window * window, float brightness);
float SDL_GetWindowBrightness(SDL_Window * window);
int SDL_SetWindowGammaRamp(SDL_Window * window,
                                                   const Uint16 * red,
                                                   const Uint16 * green,
                                                   const Uint16 * blue);
int SDL_GetWindowGammaRamp(SDL_Window * window,
                                                   Uint16 * red,
                                                   Uint16 * green,
                                                   Uint16 * blue);
typedef SDL_HitTestResult ( *SDL_HitTest)(SDL_Window *win,
                                                 const SDL_Point *area,
                                                 void *data);
int SDL_SetWindowHitTest(SDL_Window * window,
                                                 SDL_HitTest callback,
                                                 void *callback_data);
void SDL_DestroyWindow(SDL_Window * window);
SDL_bool SDL_IsScreenSaverEnabled(void);
void SDL_EnableScreenSaver(void);
void SDL_DisableScreenSaver(void);
int SDL_GL_LoadLibrary(const char *path);
void * SDL_GL_GetProcAddress(const char *proc);
void SDL_GL_UnloadLibrary(void);
SDL_bool SDL_GL_ExtensionSupported(const char
                                                           *extension);
void SDL_GL_ResetAttributes(void);
int SDL_GL_SetAttribute(SDL_GLattr attr, int value);
int SDL_GL_GetAttribute(SDL_GLattr attr, int *value);
SDL_GLContext SDL_GL_CreateContext(SDL_Window *
                                                           window);
int SDL_GL_MakeCurrent(SDL_Window * window,
                                               SDL_GLContext context);
SDL_Window* SDL_GL_GetCurrentWindow(void);
SDL_GLContext SDL_GL_GetCurrentContext(void);
void SDL_GL_GetDrawableSize(SDL_Window * window, int *w,
                                                    int *h);
int SDL_GL_SetSwapInterval(int interval);
int SDL_GL_GetSwapInterval(void);
void SDL_GL_SwapWindow(SDL_Window * window);
void SDL_GL_DeleteContext(SDL_GLContext context);
typedef Sint32 SDL_Keycode;
typedef struct SDL_Keysym
{
    SDL_Scancode scancode;
    SDL_Keycode sym;
    Uint16 mod;
    Uint32 unused;
} SDL_Keysym;
SDL_Window * SDL_GetKeyboardFocus(void);
const Uint8 * SDL_GetKeyboardState(int *numkeys);
SDL_Keymod SDL_GetModState(void);
void SDL_SetModState(SDL_Keymod modstate);
SDL_Keycode SDL_GetKeyFromScancode(SDL_Scancode scancode);
SDL_Scancode SDL_GetScancodeFromKey(SDL_Keycode key);
const char * SDL_GetScancodeName(SDL_Scancode scancode);
SDL_Scancode SDL_GetScancodeFromName(const char *name);
const char * SDL_GetKeyName(SDL_Keycode key);
SDL_Keycode SDL_GetKeyFromName(const char *name);
void SDL_StartTextInput(void);
SDL_bool SDL_IsTextInputActive(void);
void SDL_StopTextInput(void);
void SDL_SetTextInputRect(SDL_Rect *rect);
SDL_bool SDL_HasScreenKeyboardSupport(void);
SDL_bool SDL_IsScreenKeyboardShown(SDL_Window *window);
typedef struct SDL_Cursor SDL_Cursor;
SDL_Window * SDL_GetMouseFocus(void);
Uint32 SDL_GetMouseState(int *x, int *y);
Uint32 SDL_GetGlobalMouseState(int *x, int *y);
Uint32 SDL_GetRelativeMouseState(int *x, int *y);
void SDL_WarpMouseInWindow(SDL_Window * window,
                                                   int x, int y);
int SDL_WarpMouseGlobal(int x, int y);
int SDL_SetRelativeMouseMode(SDL_bool enabled);
int SDL_CaptureMouse(SDL_bool enabled);
SDL_bool SDL_GetRelativeMouseMode(void);
SDL_Cursor * SDL_CreateCursor(const Uint8 * data,
                                                     const Uint8 * mask,
                                                     int w, int h, int hot_x,
                                                     int hot_y);
SDL_Cursor * SDL_CreateColorCursor(SDL_Surface *surface,
                                                          int hot_x,
                                                          int hot_y);
SDL_Cursor * SDL_CreateSystemCursor(SDL_SystemCursor id);
void SDL_SetCursor(SDL_Cursor * cursor);
SDL_Cursor * SDL_GetCursor(void);
SDL_Cursor * SDL_GetDefaultCursor(void);
void SDL_FreeCursor(SDL_Cursor * cursor);
int SDL_ShowCursor(int toggle);
struct _SDL_Joystick;
typedef struct _SDL_Joystick SDL_Joystick;
typedef struct {
    Uint8 data[16];
} SDL_JoystickGUID;
typedef Sint32 SDL_JoystickID;
int SDL_NumJoysticks(void);
const char * SDL_JoystickNameForIndex(int device_index);
SDL_Joystick * SDL_JoystickOpen(int device_index);
SDL_Joystick * SDL_JoystickFromInstanceID(SDL_JoystickID joyid);
const char * SDL_JoystickName(SDL_Joystick * joystick);
SDL_JoystickGUID SDL_JoystickGetDeviceGUID(int device_index);
SDL_JoystickGUID SDL_JoystickGetGUID(SDL_Joystick * joystick);
void SDL_JoystickGetGUIDString(SDL_JoystickGUID guid, char *pszGUID, int cbGUID);
SDL_JoystickGUID SDL_JoystickGetGUIDFromString(const char *pchGUID);
SDL_bool SDL_JoystickGetAttached(SDL_Joystick * joystick);
SDL_JoystickID SDL_JoystickInstanceID(SDL_Joystick * joystick);
int SDL_JoystickNumAxes(SDL_Joystick * joystick);
int SDL_JoystickNumBalls(SDL_Joystick * joystick);
int SDL_JoystickNumHats(SDL_Joystick * joystick);
int SDL_JoystickNumButtons(SDL_Joystick * joystick);
void SDL_JoystickUpdate(void);
int SDL_JoystickEventState(int state);
Sint16 SDL_JoystickGetAxis(SDL_Joystick * joystick,
                                                   int axis);
Uint8 SDL_JoystickGetHat(SDL_Joystick * joystick,
                                                 int hat);
int SDL_JoystickGetBall(SDL_Joystick * joystick,
                                                int ball, int *dx, int *dy);
Uint8 SDL_JoystickGetButton(SDL_Joystick * joystick,
                                                    int button);
void SDL_JoystickClose(SDL_Joystick * joystick);
SDL_JoystickPowerLevel SDL_JoystickCurrentPowerLevel(SDL_Joystick * joystick);
struct _SDL_GameController;
typedef struct _SDL_GameController SDL_GameController;
typedef struct SDL_GameControllerButtonBind
{
    SDL_GameControllerBindType bindType;
    union
    {
        int button;
        int axis;
        struct {
            int hat;
            int hat_mask;
        } hat;
    } value;
} SDL_GameControllerButtonBind;
int SDL_GameControllerAddMappingsFromRW( SDL_RWops * rw, int freerw );
int SDL_GameControllerAddMapping( const char* mappingString );
char * SDL_GameControllerMappingForGUID( SDL_JoystickGUID guid );
char * SDL_GameControllerMapping( SDL_GameController * gamecontroller );
SDL_bool SDL_IsGameController(int joystick_index);
const char * SDL_GameControllerNameForIndex(int joystick_index);
SDL_GameController * SDL_GameControllerOpen(int joystick_index);
SDL_GameController * SDL_GameControllerFromInstanceID(SDL_JoystickID joyid);
const char * SDL_GameControllerName(SDL_GameController *gamecontroller);
SDL_bool SDL_GameControllerGetAttached(SDL_GameController *gamecontroller);
SDL_Joystick * SDL_GameControllerGetJoystick(SDL_GameController *gamecontroller);
int SDL_GameControllerEventState(int state);
void SDL_GameControllerUpdate(void);
SDL_GameControllerAxis SDL_GameControllerGetAxisFromString(const char *pchString);
const char* SDL_GameControllerGetStringForAxis(SDL_GameControllerAxis axis);
SDL_GameControllerButtonBind
SDL_GameControllerGetBindForAxis(SDL_GameController *gamecontroller,
                                 SDL_GameControllerAxis axis);
Sint16
SDL_GameControllerGetAxis(SDL_GameController *gamecontroller,
                          SDL_GameControllerAxis axis);
SDL_GameControllerButton SDL_GameControllerGetButtonFromString(const char *pchString);
const char* SDL_GameControllerGetStringForButton(SDL_GameControllerButton button);
SDL_GameControllerButtonBind
SDL_GameControllerGetBindForButton(SDL_GameController *gamecontroller,
                                   SDL_GameControllerButton button);
Uint8 SDL_GameControllerGetButton(SDL_GameController *gamecontroller,
                                                          SDL_GameControllerButton button);
void SDL_GameControllerClose(SDL_GameController *gamecontroller);
typedef Sint64 SDL_TouchID;
typedef Sint64 SDL_FingerID;
typedef struct SDL_Finger
{
    SDL_FingerID id;
    float x;
    float y;
    float pressure;
} SDL_Finger;
int SDL_GetNumTouchDevices(void);
SDL_TouchID SDL_GetTouchDevice(int index);
int SDL_GetNumTouchFingers(SDL_TouchID touchID);
SDL_Finger * SDL_GetTouchFinger(SDL_TouchID touchID, int index);
typedef Sint64 SDL_GestureID;
int SDL_RecordGesture(SDL_TouchID touchId);
int SDL_SaveAllDollarTemplates(SDL_RWops *dst);
int SDL_SaveDollarTemplate(SDL_GestureID gestureId,SDL_RWops *dst);
int SDL_LoadDollarTemplates(SDL_TouchID touchId, SDL_RWops *src);
typedef struct SDL_CommonEvent
{
    Uint32 type;
    Uint32 timestamp;
} SDL_CommonEvent;
typedef struct SDL_WindowEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    Uint8 event;
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    Sint32 data1;
    Sint32 data2;
} SDL_WindowEvent;
typedef struct SDL_KeyboardEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    Uint8 state;
    Uint8 repeat;
    Uint8 padding2;
    Uint8 padding3;
    SDL_Keysym keysym;
} SDL_KeyboardEvent;
typedef struct SDL_TextEditingEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    char text[(32)];
    Sint32 start;
    Sint32 length;
} SDL_TextEditingEvent;
typedef struct SDL_TextInputEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    char text[(32)];
} SDL_TextInputEvent;
typedef struct SDL_MouseMotionEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    Uint32 which;
    Uint32 state;
    Sint32 x;
    Sint32 y;
    Sint32 xrel;
    Sint32 yrel;
} SDL_MouseMotionEvent;
typedef struct SDL_MouseButtonEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    Uint32 which;
    Uint8 button;
    Uint8 state;
    Uint8 clicks;
    Uint8 padding1;
    Sint32 x;
    Sint32 y;
} SDL_MouseButtonEvent;
typedef struct SDL_MouseWheelEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    Uint32 which;
    Sint32 x;
    Sint32 y;
    Uint32 direction;
} SDL_MouseWheelEvent;
typedef struct SDL_JoyAxisEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_JoystickID which;
    Uint8 axis;
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    Sint16 value;
    Uint16 padding4;
} SDL_JoyAxisEvent;
typedef struct SDL_JoyBallEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_JoystickID which;
    Uint8 ball;
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    Sint16 xrel;
    Sint16 yrel;
} SDL_JoyBallEvent;
typedef struct SDL_JoyHatEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_JoystickID which;
    Uint8 hat;
    Uint8 value;
    Uint8 padding1;
    Uint8 padding2;
} SDL_JoyHatEvent;
typedef struct SDL_JoyButtonEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_JoystickID which;
    Uint8 button;
    Uint8 state;
    Uint8 padding1;
    Uint8 padding2;
} SDL_JoyButtonEvent;
typedef struct SDL_JoyDeviceEvent
{
    Uint32 type;
    Uint32 timestamp;
    Sint32 which;
} SDL_JoyDeviceEvent;
typedef struct SDL_ControllerAxisEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_JoystickID which;
    Uint8 axis;
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    Sint16 value;
    Uint16 padding4;
} SDL_ControllerAxisEvent;
typedef struct SDL_ControllerButtonEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_JoystickID which;
    Uint8 button;
    Uint8 state;
    Uint8 padding1;
    Uint8 padding2;
} SDL_ControllerButtonEvent;
typedef struct SDL_ControllerDeviceEvent
{
    Uint32 type;
    Uint32 timestamp;
    Sint32 which;
} SDL_ControllerDeviceEvent;
typedef struct SDL_AudioDeviceEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 which;
    Uint8 iscapture;
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
} SDL_AudioDeviceEvent;
typedef struct SDL_TouchFingerEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_TouchID touchId;
    SDL_FingerID fingerId;
    float x;
    float y;
    float dx;
    float dy;
    float pressure;
} SDL_TouchFingerEvent;
typedef struct SDL_MultiGestureEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_TouchID touchId;
    float dTheta;
    float dDist;
    float x;
    float y;
    Uint16 numFingers;
    Uint16 padding;
} SDL_MultiGestureEvent;
typedef struct SDL_DollarGestureEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_TouchID touchId;
    SDL_GestureID gestureId;
    Uint32 numFingers;
    float error;
    float x;
    float y;
} SDL_DollarGestureEvent;
typedef struct SDL_DropEvent
{
    Uint32 type;
    Uint32 timestamp;
    char *file;
} SDL_DropEvent;
typedef struct SDL_QuitEvent
{
    Uint32 type;
    Uint32 timestamp;
} SDL_QuitEvent;
typedef struct SDL_OSEvent
{
    Uint32 type;
    Uint32 timestamp;
} SDL_OSEvent;
typedef struct SDL_UserEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    Sint32 code;
    void *data1;
    void *data2;
} SDL_UserEvent;
struct SDL_SysWMmsg;
typedef struct SDL_SysWMmsg SDL_SysWMmsg;
typedef struct SDL_SysWMEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_SysWMmsg *msg;
} SDL_SysWMEvent;
typedef union SDL_Event
{
    Uint32 type;
    SDL_CommonEvent common;
    SDL_WindowEvent window;
    SDL_KeyboardEvent key;
    SDL_TextEditingEvent edit;
    SDL_TextInputEvent text;
    SDL_MouseMotionEvent motion;
    SDL_MouseButtonEvent button;
    SDL_MouseWheelEvent wheel;
    SDL_JoyAxisEvent jaxis;
    SDL_JoyBallEvent jball;
    SDL_JoyHatEvent jhat;
    SDL_JoyButtonEvent jbutton;
    SDL_JoyDeviceEvent jdevice;
    SDL_ControllerAxisEvent caxis;
    SDL_ControllerButtonEvent cbutton;
    SDL_ControllerDeviceEvent cdevice;
    SDL_AudioDeviceEvent adevice;
    SDL_QuitEvent quit;
    SDL_UserEvent user;
    SDL_SysWMEvent syswm;
    SDL_TouchFingerEvent tfinger;
    SDL_MultiGestureEvent mgesture;
    SDL_DollarGestureEvent dgesture;
    SDL_DropEvent drop;
    Uint8 padding[56];
} SDL_Event;
void SDL_PumpEvents(void);
int SDL_PeepEvents(SDL_Event * events, int numevents,
                                           SDL_eventaction action,
                                           Uint32 minType, Uint32 maxType);
SDL_bool SDL_HasEvent(Uint32 type);
SDL_bool SDL_HasEvents(Uint32 minType, Uint32 maxType);
void SDL_FlushEvent(Uint32 type);
void SDL_FlushEvents(Uint32 minType, Uint32 maxType);
int SDL_PollEvent(SDL_Event * event);
int SDL_WaitEvent(SDL_Event * event);
int SDL_WaitEventTimeout(SDL_Event * event,
                                                 int timeout);
int SDL_PushEvent(SDL_Event * event);
typedef int ( * SDL_EventFilter) (void *userdata, SDL_Event * event);
void SDL_SetEventFilter(SDL_EventFilter filter,
                                                void *userdata);
SDL_bool SDL_GetEventFilter(SDL_EventFilter * filter,
                                                    void **userdata);
void SDL_AddEventWatch(SDL_EventFilter filter,
                                               void *userdata);
void SDL_DelEventWatch(SDL_EventFilter filter,
                                               void *userdata);
void SDL_FilterEvents(SDL_EventFilter filter,
                                              void *userdata);
Uint8 SDL_EventState(Uint32 type, int state);
Uint32 SDL_RegisterEvents(int numevents);
char * SDL_GetBasePath(void);
char * SDL_GetPrefPath(const char *org, const char *app);
struct _SDL_Haptic;
typedef struct _SDL_Haptic SDL_Haptic;
typedef struct SDL_HapticDirection
{
    Uint8 type;
    Sint32 dir[3];
} SDL_HapticDirection;
typedef struct SDL_HapticConstant
{
    Uint16 type;
    SDL_HapticDirection direction;
    Uint32 length;
    Uint16 delay;
    Uint16 button;
    Uint16 interval;
    Sint16 level;
    Uint16 attack_length;
    Uint16 attack_level;
    Uint16 fade_length;
    Uint16 fade_level;
} SDL_HapticConstant;
typedef struct SDL_HapticPeriodic
{
    Uint16 type;
    SDL_HapticDirection direction;
    Uint32 length;
    Uint16 delay;
    Uint16 button;
    Uint16 interval;
    Uint16 period;
    Sint16 magnitude;
    Sint16 offset;
    Uint16 phase;
    Uint16 attack_length;
    Uint16 attack_level;
    Uint16 fade_length;
    Uint16 fade_level;
} SDL_HapticPeriodic;
typedef struct SDL_HapticCondition
{
    Uint16 type;
    SDL_HapticDirection direction;
    Uint32 length;
    Uint16 delay;
    Uint16 button;
    Uint16 interval;
    Uint16 right_sat[3];
    Uint16 left_sat[3];
    Sint16 right_coeff[3];
    Sint16 left_coeff[3];
    Uint16 deadband[3];
    Sint16 center[3];
} SDL_HapticCondition;
typedef struct SDL_HapticRamp
{
    Uint16 type;
    SDL_HapticDirection direction;
    Uint32 length;
    Uint16 delay;
    Uint16 button;
    Uint16 interval;
    Sint16 start;
    Sint16 end;
    Uint16 attack_length;
    Uint16 attack_level;
    Uint16 fade_length;
    Uint16 fade_level;
} SDL_HapticRamp;
typedef struct SDL_HapticLeftRight
{
    Uint16 type;
    Uint32 length;
    Uint16 large_magnitude;
    Uint16 small_magnitude;
} SDL_HapticLeftRight;
typedef struct SDL_HapticCustom
{
    Uint16 type;
    SDL_HapticDirection direction;
    Uint32 length;
    Uint16 delay;
    Uint16 button;
    Uint16 interval;
    Uint8 channels;
    Uint16 period;
    Uint16 samples;
    Uint16 *data;
    Uint16 attack_length;
    Uint16 attack_level;
    Uint16 fade_length;
    Uint16 fade_level;
} SDL_HapticCustom;
typedef union SDL_HapticEffect
{
    Uint16 type;
    SDL_HapticConstant constant;
    SDL_HapticPeriodic periodic;
    SDL_HapticCondition condition;
    SDL_HapticRamp ramp;
    SDL_HapticLeftRight leftright;
    SDL_HapticCustom custom;
} SDL_HapticEffect;
int SDL_NumHaptics(void);
const char * SDL_HapticName(int device_index);
SDL_Haptic * SDL_HapticOpen(int device_index);
int SDL_HapticOpened(int device_index);
int SDL_HapticIndex(SDL_Haptic * haptic);
int SDL_MouseIsHaptic(void);
SDL_Haptic * SDL_HapticOpenFromMouse(void);
int SDL_JoystickIsHaptic(SDL_Joystick * joystick);
SDL_Haptic * SDL_HapticOpenFromJoystick(SDL_Joystick *
                                                               joystick);
void SDL_HapticClose(SDL_Haptic * haptic);
int SDL_HapticNumEffects(SDL_Haptic * haptic);
int SDL_HapticNumEffectsPlaying(SDL_Haptic * haptic);
unsigned int SDL_HapticQuery(SDL_Haptic * haptic);
int SDL_HapticNumAxes(SDL_Haptic * haptic);
int SDL_HapticEffectSupported(SDL_Haptic * haptic,
                                                      SDL_HapticEffect *
                                                      effect);
int SDL_HapticNewEffect(SDL_Haptic * haptic,
                                                SDL_HapticEffect * effect);
int SDL_HapticUpdateEffect(SDL_Haptic * haptic,
                                                   int effect,
                                                   SDL_HapticEffect * data);
int SDL_HapticRunEffect(SDL_Haptic * haptic,
                                                int effect,
                                                Uint32 iterations);
int SDL_HapticStopEffect(SDL_Haptic * haptic,
                                                 int effect);
void SDL_HapticDestroyEffect(SDL_Haptic * haptic,
                                                     int effect);
int SDL_HapticGetEffectStatus(SDL_Haptic * haptic,
                                                      int effect);
int SDL_HapticSetGain(SDL_Haptic * haptic, int gain);
int SDL_HapticSetAutocenter(SDL_Haptic * haptic,
                                                    int autocenter);
int SDL_HapticPause(SDL_Haptic * haptic);
int SDL_HapticUnpause(SDL_Haptic * haptic);
int SDL_HapticStopAll(SDL_Haptic * haptic);
int SDL_HapticRumbleSupported(SDL_Haptic * haptic);
int SDL_HapticRumbleInit(SDL_Haptic * haptic);
int SDL_HapticRumblePlay(SDL_Haptic * haptic, float strength, Uint32 length );
int SDL_HapticRumbleStop(SDL_Haptic * haptic);
SDL_bool SDL_SetHintWithPriority(const char *name,
                                                         const char *value,
                                                         SDL_HintPriority priority);
SDL_bool SDL_SetHint(const char *name,
                                             const char *value);
const char * SDL_GetHint(const char *name);
typedef void (*SDL_HintCallback)(void *userdata, const char *name, const char *oldValue, const char *newValue);
void SDL_AddHintCallback(const char *name,
                                                 SDL_HintCallback callback,
                                                 void *userdata);
void SDL_DelHintCallback(const char *name,
                                                 SDL_HintCallback callback,
                                                 void *userdata);
void SDL_ClearHints(void);
void * SDL_LoadObject(const char *sofile);
void * SDL_LoadFunction(void *handle,
                                               const char *name);
void SDL_UnloadObject(void *handle);
void SDL_LogSetAllPriority(SDL_LogPriority priority);
void SDL_LogSetPriority(int category,
                                                SDL_LogPriority priority);
SDL_LogPriority SDL_LogGetPriority(int category);
void SDL_LogResetPriorities(void);
void SDL_Log( const char *fmt, ...);
void SDL_LogVerbose(int category, const char *fmt, ...);
void SDL_LogDebug(int category, const char *fmt, ...);
void SDL_LogInfo(int category, const char *fmt, ...);
void SDL_LogWarn(int category, const char *fmt, ...);
void SDL_LogError(int category, const char *fmt, ...);
void SDL_LogCritical(int category, const char *fmt, ...);
void SDL_LogMessage(int category,
                                            SDL_LogPriority priority,
                                                                     const char *fmt, ...);
typedef void (*SDL_LogOutputFunction)(void *userdata, int category, SDL_LogPriority priority, const char *message);
void SDL_LogGetOutputFunction(SDL_LogOutputFunction *callback, void **userdata);
void SDL_LogSetOutputFunction(SDL_LogOutputFunction callback, void *userdata);
typedef struct
{
    Uint32 flags;
    int buttonid;
    const char * text;
} SDL_MessageBoxButtonData;
typedef struct
{
    Uint8 r, g, b;
} SDL_MessageBoxColor;
typedef struct
{
    SDL_MessageBoxColor colors[SDL_MESSAGEBOX_COLOR_MAX];
} SDL_MessageBoxColorScheme;
typedef struct
{
    Uint32 flags;
    SDL_Window *window;
    const char *title;
    const char *message;
    int numbuttons;
    const SDL_MessageBoxButtonData *buttons;
    const SDL_MessageBoxColorScheme *colorScheme;
} SDL_MessageBoxData;
int SDL_ShowMessageBox(const SDL_MessageBoxData *messageboxdata, int *buttonid);
int SDL_ShowSimpleMessageBox(Uint32 flags, const char *title, const char *message, SDL_Window *window);
SDL_PowerState SDL_GetPowerInfo(int *secs, int *pct);
typedef struct SDL_RendererInfo
{
    const char *name;
    Uint32 flags;
    Uint32 num_texture_formats;
    Uint32 texture_formats[16];
    int max_texture_width;
    int max_texture_height;
} SDL_RendererInfo;
struct SDL_Renderer;
typedef struct SDL_Renderer SDL_Renderer;
struct SDL_Texture;
typedef struct SDL_Texture SDL_Texture;
int SDL_GetNumRenderDrivers(void);
int SDL_GetRenderDriverInfo(int index,
                                                    SDL_RendererInfo * info);
int SDL_CreateWindowAndRenderer(
                                int width, int height, Uint32 window_flags,
                                SDL_Window **window, SDL_Renderer **renderer);
SDL_Renderer * SDL_CreateRenderer(SDL_Window * window,
                                               int index, Uint32 flags);
SDL_Renderer * SDL_CreateSoftwareRenderer(SDL_Surface * surface);
SDL_Renderer * SDL_GetRenderer(SDL_Window * window);
int SDL_GetRendererInfo(SDL_Renderer * renderer,
                                                SDL_RendererInfo * info);
int SDL_GetRendererOutputSize(SDL_Renderer * renderer,
                                                      int *w, int *h);
SDL_Texture * SDL_CreateTexture(SDL_Renderer * renderer,
                                                        Uint32 format,
                                                        int access, int w,
                                                        int h);
SDL_Texture * SDL_CreateTextureFromSurface(SDL_Renderer * renderer, SDL_Surface * surface);
int SDL_QueryTexture(SDL_Texture * texture,
                                             Uint32 * format, int *access,
                                             int *w, int *h);
int SDL_SetTextureColorMod(SDL_Texture * texture,
                                                   Uint8 r, Uint8 g, Uint8 b);
int SDL_GetTextureColorMod(SDL_Texture * texture,
                                                   Uint8 * r, Uint8 * g,
                                                   Uint8 * b);
int SDL_SetTextureAlphaMod(SDL_Texture * texture,
                                                   Uint8 alpha);
int SDL_GetTextureAlphaMod(SDL_Texture * texture,
                                                   Uint8 * alpha);
int SDL_SetTextureBlendMode(SDL_Texture * texture,
                                                    SDL_BlendMode blendMode);
int SDL_GetTextureBlendMode(SDL_Texture * texture,
                                                    SDL_BlendMode *blendMode);
int SDL_UpdateTexture(SDL_Texture * texture,
                                              const SDL_Rect * rect,
                                              const void *pixels, int pitch);
int SDL_UpdateYUVTexture(SDL_Texture * texture,
                                                 const SDL_Rect * rect,
                                                 const Uint8 *Yplane, int Ypitch,
                                                 const Uint8 *Uplane, int Upitch,
                                                 const Uint8 *Vplane, int Vpitch);
int SDL_LockTexture(SDL_Texture * texture,
                                            const SDL_Rect * rect,
                                            void **pixels, int *pitch);
void SDL_UnlockTexture(SDL_Texture * texture);
SDL_bool SDL_RenderTargetSupported(SDL_Renderer *renderer);
int SDL_SetRenderTarget(SDL_Renderer *renderer,
                                                SDL_Texture *texture);
SDL_Texture * SDL_GetRenderTarget(SDL_Renderer *renderer);
int SDL_RenderSetLogicalSize(SDL_Renderer * renderer, int w, int h);
void SDL_RenderGetLogicalSize(SDL_Renderer * renderer, int *w, int *h);
int SDL_RenderSetViewport(SDL_Renderer * renderer,
                                                  const SDL_Rect * rect);
void SDL_RenderGetViewport(SDL_Renderer * renderer,
                                                   SDL_Rect * rect);
int SDL_RenderSetClipRect(SDL_Renderer * renderer,
                                                  const SDL_Rect * rect);
void SDL_RenderGetClipRect(SDL_Renderer * renderer,
                                                   SDL_Rect * rect);
SDL_bool SDL_RenderIsClipEnabled(SDL_Renderer * renderer);
int SDL_RenderSetScale(SDL_Renderer * renderer,
                                               float scaleX, float scaleY);
void SDL_RenderGetScale(SDL_Renderer * renderer,
                                               float *scaleX, float *scaleY);
int SDL_SetRenderDrawColor(SDL_Renderer * renderer,
                                           Uint8 r, Uint8 g, Uint8 b,
                                           Uint8 a);
int SDL_GetRenderDrawColor(SDL_Renderer * renderer,
                                           Uint8 * r, Uint8 * g, Uint8 * b,
                                           Uint8 * a);
int SDL_SetRenderDrawBlendMode(SDL_Renderer * renderer,
                                                       SDL_BlendMode blendMode);
int SDL_GetRenderDrawBlendMode(SDL_Renderer * renderer,
                                                       SDL_BlendMode *blendMode);
int SDL_RenderClear(SDL_Renderer * renderer);
int SDL_RenderDrawPoint(SDL_Renderer * renderer,
                                                int x, int y);
int SDL_RenderDrawPoints(SDL_Renderer * renderer,
                                                 const SDL_Point * points,
                                                 int count);
int SDL_RenderDrawLine(SDL_Renderer * renderer,
                                               int x1, int y1, int x2, int y2);
int SDL_RenderDrawLines(SDL_Renderer * renderer,
                                                const SDL_Point * points,
                                                int count);
int SDL_RenderDrawRect(SDL_Renderer * renderer,
                                               const SDL_Rect * rect);
int SDL_RenderDrawRects(SDL_Renderer * renderer,
                                                const SDL_Rect * rects,
                                                int count);
int SDL_RenderFillRect(SDL_Renderer * renderer,
                                               const SDL_Rect * rect);
int SDL_RenderFillRects(SDL_Renderer * renderer,
                                                const SDL_Rect * rects,
                                                int count);
int SDL_RenderCopy(SDL_Renderer * renderer,
                                           SDL_Texture * texture,
                                           const SDL_Rect * srcrect,
                                           const SDL_Rect * dstrect);
int SDL_RenderCopyEx(SDL_Renderer * renderer,
                                           SDL_Texture * texture,
                                           const SDL_Rect * srcrect,
                                           const SDL_Rect * dstrect,
                                           const double angle,
                                           const SDL_Point *center,
                                           const SDL_RendererFlip flip);
int SDL_RenderReadPixels(SDL_Renderer * renderer,
                                                 const SDL_Rect * rect,
                                                 Uint32 format,
                                                 void *pixels, int pitch);
void SDL_RenderPresent(SDL_Renderer * renderer);
void SDL_DestroyTexture(SDL_Texture * texture);
void SDL_DestroyRenderer(SDL_Renderer * renderer);
int SDL_GL_BindTexture(SDL_Texture *texture, float *texw, float *texh);
int SDL_GL_UnbindTexture(SDL_Texture *texture);
Uint32 SDL_GetTicks(void);
Uint64 SDL_GetPerformanceCounter(void);
Uint64 SDL_GetPerformanceFrequency(void);
void SDL_Delay(Uint32 ms);
typedef Uint32 ( * SDL_TimerCallback) (Uint32 interval, void *param);
typedef int SDL_TimerID;
SDL_TimerID SDL_AddTimer(Uint32 interval,
                                                 SDL_TimerCallback callback,
                                                 void *param);
SDL_bool SDL_RemoveTimer(SDL_TimerID id);
typedef struct SDL_version
{
    Uint8 major;
    Uint8 minor;
    Uint8 patch;
} SDL_version;
void SDL_GetVersion(SDL_version * ver);
const char * SDL_GetRevision(void);
int SDL_GetRevisionNumber(void);
int SDL_Init(Uint32 flags);
int SDL_InitSubSystem(Uint32 flags);
void SDL_QuitSubSystem(Uint32 flags);
Uint32 SDL_WasInit(Uint32 flags);
void SDL_Quit(void);