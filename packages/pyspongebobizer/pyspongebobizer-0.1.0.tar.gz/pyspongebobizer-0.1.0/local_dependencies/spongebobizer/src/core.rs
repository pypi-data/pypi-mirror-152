use std::iter::FusedIterator;
use std::mem;

pub(crate) struct ConversionIterator {
	inner: [u32; 3]
}

impl From<[u32; 2]> for ConversionIterator /* {{{ */ {
	fn from(inner: [u32; 2]) -> Self {
		Self::from([inner[0], inner[1], 0])
	}
} // }}}

impl From<[u32; 3]> for ConversionIterator /* {{{ */ {
	fn from(inner: [u32; 3]) -> Self {
		Self{inner}
	}
} // }}}

impl Iterator for ConversionIterator {
	type Item = char;

	fn next(&mut self) -> Option<Self::Item> /* {{{ */ {
		if(self.inner[0] == 0) {
			return None;
		}
		let value = mem::take(&mut self.inner[0]);
		self.inner.rotate_left(1);
		// SAFETY:  Because this strictly comes from unicode_case_mapping::to_uppercase() and
		// unicode_case_mapping::to_lowercase(), we can only possibly have valid chars
		Some(unsafe { char::from_u32_unchecked(value) })
	} // }}}

	fn size_hint(&self) -> (usize, Option<usize>) /* {{{ */ {
		let mut size = 0;
		for i in 0..3 {
			if(self.inner[i] == 0) {
				break;
			}
			size += 1;
		}
		(size, Some(size))
	} // }}}
}

impl ExactSizeIterator for ConversionIterator {}
impl FusedIterator for ConversionIterator {}

pub(crate) enum Char {
	Ascii(Option<char>),
	NonAscii(ConversionIterator),
}

impl Iterator for Char /* {{{ */ {
	type Item = char;

	fn next(&mut self) -> Option<Self::Item> {
		match self {
			Self::Ascii(i) => i.take(),
			Self::NonAscii(i) => i.next(),
		}
	}

	fn count(self) -> usize {
		match self {
			Self::Ascii(Some(_)) => 1,
			Self::Ascii(None) => 0,
			Self::NonAscii(inner) => inner.count(),
		}
	}

	fn size_hint(&self) -> (usize, Option<usize>) {
		match self {
			Self::Ascii(Some(_)) => (1, Some(1)),
			Self::Ascii(None) => (0, Some(0)),
			Self::NonAscii(inner) => inner.size_hint(),
		}
	}
} // }}}

impl ExactSizeIterator for Char {}
impl FusedIterator for Char {}

impl From<char> for Char /* {{{ */ {
	fn from(inner: char) -> Self {
		Self::Ascii(Some(inner))
	}
} // }}}

impl From<[u32; 2]> for Char /* {{{ */ {
	fn from(inner: [u32; 2]) -> Self {
		Self::NonAscii(inner.into())
	}
} // }}}

impl From<[u32; 3]> for Char /* {{{ */ {
	fn from(inner: [u32; 3]) -> Self {
		Self::NonAscii(inner.into())
	}
} // }}}

#[derive(Clone, Copy, Eq, PartialEq)]
pub(crate) enum AlphaCase {
	Upper,
	Lower
}

impl AlphaCase {
	pub(crate) fn negate(&mut self) {
		*self = match self {
			Self::Upper => Self::Lower,
			Self::Lower => Self::Upper
		}
	}
}

fn to_uppercase(c: char) -> Char {
	match unicode_case_mapping::to_uppercase(c) {
		[0, ..] => c.into(),
		v => v.into()
	}
}

fn to_lowercase(c: char) -> Char {
	match unicode_case_mapping::to_lowercase(c) {
		[0, ..] => c.into(),
		v => v.into()
	}
}

pub(crate) fn convert_char(c: char, into: &AlphaCase) -> Char {
	match (c.is_ascii(), into) {
		(true, AlphaCase::Upper) => c.to_ascii_uppercase().into(),
		(true, AlphaCase::Lower) => c.to_ascii_lowercase().into(),
		(false, AlphaCase::Upper) => to_uppercase(c),
		(false, AlphaCase::Lower) => to_lowercase(c)
	}
}

