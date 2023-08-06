#![allow(unused_parens)]
mod core;
mod processor;
pub use processor::Spongebobizer;
mod r#trait;
pub use r#trait::Spongebobize;

#[inline(never)] // Not sure why, but if this ever gets inlined, it _tanks_ performance.
pub fn process_string(input: &str) -> String {
	input.spongebobize().collect()
}

#[cfg(test)]
mod tests /* {{{ */ {
	use focaccia::CaseFold;
	use test_strategy::proptest;
	use super::*;

	#[test]
	fn process_lorem_ipsum() {
		assert_eq!(process_string("lorem ipsum"), "lOrEm iPsuM");
		let mut iter = "lorem ipsum".spongebobize();
		assert_eq!(iter.next(), Some('l'));
		assert_eq!(iter.next(), Some('O'));
		assert_eq!(iter.next(), Some('r'));
		assert_eq!(iter.next(), Some('E'));
		assert_eq!(iter.next(), Some('m'));
		assert_eq!(iter.next(), Some(' '));
		assert_eq!(iter.next(), Some('i'));
		assert_eq!(iter.next(), Some('P'));
		assert_eq!(iter.next(), Some('s'));
		assert_eq!(iter.next(), Some('u'));
		assert_eq!(iter.next(), Some('M'));
		assert_eq!(iter.next(), None);
	}

	#[test]
	fn test_abc123xyz() {
		assert_eq!(process_string("abc123xyz"), "aBc123XyZ");
	}

	#[test]
	fn test_random_unicode() {
		assert_eq!(process_string("8ʨ%ƴԑ:֍ыȘB\"[QןGg"), "8ʨ%ƴԐ:֍ыȘb\"[QןGg");
		assert_eq!(process_string("Hӆ͑wuƂƳ=קfԵ}l߆+È"), "Hӆ͑WuƂƳ=קFե}l߆+È");
	}

	#[test]
	fn test_nonalphabetic() {
		assert_eq!(
			process_string("1234567890)(*&^%$#@! []\\|}{';:\"/.,?><`~"),
			"1234567890)(*&^%$#@! []\\|}{';:\"/.,?><`~"
		);
	}

	#[proptest]
	fn random(input: String) {
		let full = CaseFold::Full;
		let turkic = CaseFold::Turkic;
		let output = input.spongebobize().collect::<String>();
		let input_num = input.chars().map(|c| c as u32).collect::<Vec<_>>();
		let output_num = output.chars().map(|c| c as u32).collect::<Vec<_>>();
		dbg!(&input, &output);
		dbg!(&input_num, &output_num);
		assert!(
			full.case_eq(&input, &output) ||
			turkic.case_eq(&input, &output)
		);
	}
} // }}}

