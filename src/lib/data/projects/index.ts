import { filterProjects, importProjects } from './utils';

export const allProjects = importProjects(true);
export const filteredProjects = filterProjects(allProjects);
