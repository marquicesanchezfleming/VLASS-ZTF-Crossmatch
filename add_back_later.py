
def plot_ls_cutout(ddir, name, ra_str, dec_str, outputf):
    """ Plot cutout from Legacy Survey """
    # Create a SkyCoord object from ra_str and dec_str
    coord = SkyCoord(ra_str, dec_str, unit=("hour", "degree"))

    fname = os.path.join(ddir, f"{name}_LegSurvey.png")

    if not os.path.isfile(fname):
        url = f"http://legacysurvey.org/viewer/cutout.jpg?ra={coord.ra.deg}&dec={coord.dec.deg}&layer=ls-dr9&pixscale=0.27&bands=grz"
        plt.figure(figsize=(2.1, 2.1), dpi=120)
        try:
            r = requests.get(url)
            img = Image.open(io.BytesIO(r.content))
            plt.imshow(img)
            plt.title("LegSurv DR9", fontsize=12)
            plt.axis('off')
            plt.tight_layout()
            plt.savefig(fname, bbox_inches="tight")

            decsign = '+' if coord.dec.deg >= 0 else '-'
            lslinkstr = f"http://legacysurvey.org/viewer?ra={coord.ra.deg:.6f}&dec={decsign}{abs(coord.dec.deg):.6f}&zoom=16&layer=dr9"
            outputf.write(f"<a href='{lslinkstr}'>")
            outputf.write(f'<img src="{name}_LegSurvey.png" height="200">')
            outputf.write("</a>")
            outputf.write('<br>')
        except Exception as e:
            # Not in footprint or another error
            print(f"Error: {e}")
            return None
        finally:
            plt.close()

    return fname

def plot_ps1_cutout(ddir, name, ra_str, dec_str, outputf):
    """ Plot cutout from PanSTARRS """
    # Create a SkyCoord object from ra_str and dec_str
    coord = SkyCoord(ra_str, dec_str, unit=("hour", "degree"))

    fname = os.path.join(ddir, f"{name}_ps1.png")

    if not os.path.isfile(fname):
        img = stamps.get_ps_stamp(coord.ra.deg, coord.dec.deg, size=240, color=["y", "g", "i"])
        plt.figure(figsize=(2.1, 2.1), dpi=120)
        plt.imshow(np.asarray(img))
        plt.title("PS1 (y/g/i)", fontsize=12)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(fname, bbox_inches="tight")

        decsign = '+' if coord.dec.deg >= 0 else '-'
        pslinkstr = f"https://ps1images.stsci.edu/cgi-bin/ps1cutouts?ra={coord.ra.deg:.6f}&dec={decsign}{abs(coord.dec.deg):.6f}&size=240&format=jpeg&filters=ygi"
        outputf.write(f"<a href='{pslinkstr}'>")
        outputf.write(f'<img src="{name}_ps1.png" height="200">')
        outputf.write("</a>")
        outputf.write('<br>')
        plt.close()
