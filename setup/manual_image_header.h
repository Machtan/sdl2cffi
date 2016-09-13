const SDL_version * IMG_Linked_Version(void);

typedef enum
{
    IMG_INIT_JPG = 0x00000001,
    IMG_INIT_PNG = 0x00000002,
    IMG_INIT_TIF = 0x00000004,
    IMG_INIT_WEBP = 0x00000008
} IMG_InitFlags;

/* Loads dynamic libraries and prepares them for use.  Flags should be
   one or more flags from IMG_InitFlags OR'd together.
   It returns the flags successfully initialized, or 0 on failure.
 */
int IMG_Init(int flags);

/* Unloads libraries loaded with IMG_Init */
void IMG_Quit(void);

/* Load an image from an SDL data source.
   The 'type' may be one of: "BMP", "GIF", "PNG", etc.

   If the image format supports a transparent pixel, SDL will set the
   colorkey for the surface.  You can enable RLE acceleration on the
   surface afterwards by calling:
    SDL_SetColorKey(image, SDL_RLEACCEL, image->format->colorkey);
 */
SDL_Surface * IMG_LoadTyped_RW(SDL_RWops *src, int freesrc, const char *type);
/* Convenience functions */
SDL_Surface * IMG_Load(const char *file);
SDL_Surface * IMG_Load_RW(SDL_RWops *src, int freesrc);

/* Load an image directly into a render texture.
 */
SDL_Texture * IMG_LoadTexture(SDL_Renderer *renderer, const char *file);
SDL_Texture * IMG_LoadTexture_RW(SDL_Renderer *renderer, SDL_RWops *src, int freesrc);
SDL_Texture * IMG_LoadTextureTyped_RW(SDL_Renderer *renderer, SDL_RWops *src, int freesrc, const char *type);

/* Functions to detect a file type, given a seekable source */
int IMG_isICO(SDL_RWops *src);
int IMG_isCUR(SDL_RWops *src);
int IMG_isBMP(SDL_RWops *src);
int IMG_isGIF(SDL_RWops *src);
int IMG_isJPG(SDL_RWops *src);
int IMG_isLBM(SDL_RWops *src);
int IMG_isPCX(SDL_RWops *src);
int IMG_isPNG(SDL_RWops *src);
int IMG_isPNM(SDL_RWops *src);
int IMG_isTIF(SDL_RWops *src);
int IMG_isXCF(SDL_RWops *src);
int IMG_isXPM(SDL_RWops *src);
int IMG_isXV(SDL_RWops *src);
int IMG_isWEBP(SDL_RWops *src);

/* Individual loading functions */
SDL_Surface * IMG_LoadICO_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadCUR_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadBMP_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadGIF_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadJPG_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadLBM_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadPCX_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadPNG_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadPNM_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadTGA_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadTIF_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadXCF_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadXPM_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadXV_RW(SDL_RWops *src);
SDL_Surface * IMG_LoadWEBP_RW(SDL_RWops *src);

SDL_Surface * IMG_ReadXPMFromArray(char **xpm);

/* Individual saving functions */
int IMG_SavePNG(SDL_Surface *surface, const char *file);
int IMG_SavePNG_RW(SDL_Surface *surface, SDL_RWops *dst, int freedst);