import { filteredProjects } from '$lib/data/projects';

export async function load() {
	return {
		projects: filteredProjects
	};
}
