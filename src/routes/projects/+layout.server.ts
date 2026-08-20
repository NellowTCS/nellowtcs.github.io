import { allProjects } from '$lib/data/projects';

export async function load({ url }: { url: { pathname: string } }) {
	const { pathname } = url;
	const slug = pathname.replace('/projects/', '');
	if (!slug || slug === 'projects') return { project: undefined };
	const project = allProjects.find((p) => p.slug === slug);

	return {
		project
	};
}
