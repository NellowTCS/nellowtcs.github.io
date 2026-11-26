// Base values for meta tags
// So they can be added as suffixes on different pages
// Via <svelte:head>

export const siteBaseUrl = 'https://nellowtcs.me/';

export const absoluteUrl = (path = '') => new URL(path.replace(/^\/+/, ''), siteBaseUrl).toString();

export const keywords = ['Developer', 'Projects', 'Blog', 'Web', 'Static Site'];

export const description =
	"The personal site and blog of NellowTCS: open source projects, browser engines, Rust parsers, and whatever else I'm working on.";

export const title = 'Home | NellowTCS';

export const image = absoluteUrl('/images/site-preview.png');
