from data_structures.hash_table import LinearProbeTable

def valid_anagram(s: str, t: str) -> bool:
	s_letter_cnt = LinearProbeTable()
	t_letter_cnt = LinearProbeTable()

	for ch in s:
		if ch in s_letter_cnt:
			s_letter_cnt[ch] += 1
		else:
			s_letter_cnt[ch] = 1

	for ch in t:
		if ch in t_letter_cnt:
			t_letter_cnt[ch] += 1
		else:
			t_letter_cnt[ch] = 1
		
	for ch in s:
		if ch not in t_letter_cnt or t_letter_cnt[ch] != s_letter_cnt[ch]:
			return False
	
	return len(s) == len(t) # Ensure they have the same length (otherwise s is a subset of t)


if __name__ == "__main__": 
	valid_anagram("anagram", "nagaram")
	pass