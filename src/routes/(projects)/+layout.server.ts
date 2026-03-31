import { filteredProjects } from '$lib/data/projects';

export async function load({ url }: { url: { pathname: string } }) {
	const { pathname } = url;
	const slug = pathname.replace('/', '');
	const project = filteredProjects.find((p) => p.slug === slug);

	return {
		project
	};
}
