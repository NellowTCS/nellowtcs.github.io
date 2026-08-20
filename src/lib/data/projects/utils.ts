import type { Component } from 'svelte';
import { render as svelteRender } from 'svelte/server';
import type { Project } from '$lib/utils/types';

export const importProjects = (render = false) => {
	const blogImports = import.meta.glob('$routes/*/*/*.md', { eager: true });
	const innerImports = import.meta.glob('$routes/*/*/*/*.md', { eager: true });

	const imports = { ...blogImports, ...innerImports };

	const projects: Project[] = [];
	for (const path in imports) {
		if (
			path.includes('/projects/') &&
			!path.endsWith('+layout.server.ts') &&
			!path.endsWith('+layout.svelte')
		) {
			const project = imports[path] as { metadata: Record<string, unknown>; default?: Component };
			if (project) {
				projects.push({
					...project.metadata,
					html: render && project.default ? svelteRender(project.default).html : undefined
				});
			}
		}
	}

	return projects;
};

export const filterProjects = (projects: Project[]) => {
	return projects
		.filter((project) => !project.hidden)
		.sort((a, b) =>
			new Date(a.date).getTime() > new Date(b.date).getTime()
				? -1
				: new Date(a.date).getTime() < new Date(b.date).getTime()
					? 1
					: 0
		);
};

export const allProjects = importProjects(true);
export const filteredProjects = filterProjects(allProjects);
