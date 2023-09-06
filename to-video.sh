mkdir -p out/hist out/img

# Render with 4 threads
{ python main.py 0 60 & python main.py 60 120 & python main.py 120 180 & python main.py 180 240; }


for f in out/img/*tiff; do
	convert "$f" "$(echo $f | sed 's:tiff:png:')"
	echo "$f -> $(echo $f | sed 's:tiff:png:')"
done

ffmpeg -y -pattern_type glob -i 'out/hist/*.png' -framerate 24 -c:v libx264 -crf 0 out.hist.mkv

ffmpeg -y -pattern_type glob -i 'out/img/*.png' -framerate 24 -c:v libx264 -crf 0 out.img.mkv

# what the fuck
ffmpeg -y -i out.img.mkv -i out.hist.mkv -filter_complex \
	"[0][1]scale2ref='oh*mdar':'if(lt(main_h,ih),ih,main_h)'[0s][1s];
	[1s][0s]scale2ref='oh*mdar':'if(lt(main_h,ih),ih,main_h)'[1s][0s];
	[0s][1s]hstack,setsar=1,framerate=24" \
	out/output.mkv
