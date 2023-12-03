#!bin/awk 
BEGIN {
	count=0;
}
{
	arraylen=0;
	split($0, chars, "")
	for (i=1; i <= length($0); i++) {
		if(chars[i] ~ /^[0-9]/){
			array[arraylen++] = chars[i];	
		}
		
	}
	count += array[0]*10 + array[arraylen-1];
}
END{
	printf(count);
}





