<script lang="ts">
	import ContentSection from '$lib/components/organisms/ContentSection.svelte';
	import ProjectCard from '$lib/components/molecules/ProjectCard.svelte';
	import type { Project } from '$lib/utils/types';
	import { siteBaseUrl } from '$lib/data/meta';

	export let data: {
		projects: Project[];
	};

	let { projects } = data;
</script>

<svelte:head>
	<title>Projects | NellowTCS</title>
	<meta
		name="description"
		content="Open source projects, libraries, and tools by NellowTCS. Browser engines, Obsidian plugins, Rust parsers, embedded systems, and more."
	/>
	<link rel="canonical" href="{siteBaseUrl}projects" />
	<meta property="og:title" content="Projects | NellowTCS" />
	<meta
		property="og:description"
		content="Open source projects, libraries, and tools by NellowTCS. Browser engines, Obsidian plugins, Rust parsers, embedded systems, and more."
	/>
	<meta property="og:url" content="{siteBaseUrl}projects" />
	<meta property="og:type" content="website" />
	<meta name="twitter:title" content="Projects | NellowTCS" />
	<meta
		name="twitter:description"
		content="Open source projects, libraries, and tools by NellowTCS. Browser engines, Obsidian plugins, Rust parsers, embedded systems, and more."
	/>
</svelte:head>

<div class="container">
	<h1>Projects</h1>
	<ContentSection description="Check out what I've been working on.">
		<div class="grid">
			{#each projects as project (project.slug)}
				<ProjectCard
					title={project.title}
					coverImage={project.coverImage}
					excerpt={project.excerpt}
					slug={project.slug}
					tags={project.tags}
					link={project.link}
					repo={project.repo}
					docs={project.docs}
					npm={project.npm}
					cargo={project.cargo}
				/>
			{/each}
		</div>
	</ContentSection>
</div>

<style lang="scss">
	@use '$lib/scss/mixins' as *;

	.grid {
		width: 100%;
		display: grid;
		grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
		grid-gap: 20px;

		@include for-tablet-portrait-down {
			grid-template-columns: 1fr;
		}

		@include for-tablet-landscape-up {
			> :global(:nth-child(6n + 1)) {
				grid-column: span 6;
			}
			> :global(:nth-child(6n + 2)) {
				grid-column: span 3;
			}
			> :global(:nth-child(6n + 3)) {
				grid-column: span 3;
			}
			> :global(:nth-child(6n + 4)),
			:global(:nth-child(6n + 5)),
			:global(:nth-child(6n + 6)) {
				grid-column: span 2;
			}
		}
	}
</style>
