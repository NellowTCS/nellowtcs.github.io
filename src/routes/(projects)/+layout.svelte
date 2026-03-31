<script lang="ts">
	import Header from '$lib/components/organisms/Header.svelte';
	import Footer from '$lib/components/organisms/Footer.svelte';
	import Tag from '$lib/components/atoms/Tag.svelte';
	import Button from '$lib/components/atoms/Button.svelte';
	import Image from '$lib/components/atoms/Image.svelte';
	import dateformat from 'dateformat';
	import type { Project } from '$lib/utils/types';

	export let data: { project: Project };
	$: ({ project } = data);
</script>

<svelte:head>
	<title>{project.title} - Projects</title>
	<meta name="description" content={project.excerpt} />
</svelte:head>

<div class="article-layout">
	<Header showBackground />

	<main>
		<article id="article-content">
			<div class="header">
				<h1>{project.title}</h1>
				<div class="note">Started on {dateformat(project.date, 'UTC:dd mmmm yyyy')}</div>
				{#if project.tags?.length}
					<div class="tags">
						{#each project.tags as tag}
							<Tag>{tag}</Tag>
						{/each}
					</div>
				{/if}
			</div>

			{#if project.coverImage}
				<div class="cover-image">
					<Image src={project.coverImage} alt={project.title} />
				</div>
			{/if}

			<div class="links">
				{#if project.link}
					<Button href={project.link}>Live Demo</Button>
				{/if}
				{#if project.repo}
					<Button href={project.repo} color="secondary">GitHub</Button>
				{/if}
			</div>

			<div class="content">
				<slot />
			</div>
		</article>
	</main>

	<Footer />
</div>

<style lang="scss">
	@import '$lib/scss/_mixins.scss';

	.article-layout {
		--body-background-color: var(--color--post-page-background);
		background-color: var(--color--post-page-background);
	}

	#article-content {
		--main-column-width: 65ch;
		position: relative;
		padding-top: 40px;
		padding-bottom: 80px;
		padding-right: 15px;
		padding-left: 15px;

		@include for-iphone-se {
			padding-left: 0;
			padding-right: 0;
		}

		@include for-tablet-portrait-up {
			padding-right: 20px;
			padding-left: 20px;
		}

		@include for-tablet-landscape-up {
			padding-right: 30px;
			padding-left: 30px;
		}

		display: flex;
		flex-direction: column;
		gap: 30px;

		.header {
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			text-align: center;
			gap: 10px;
			width: min(var(--main-column-width), 100%);
			margin: 0 auto;

			.note {
				font-size: 90%;
				color: rgba(var(--color--text-rgb), 0.8);
			}
		}

		.cover-image {
			width: min(var(--main-column-width), 100%);
			margin: 0 auto;
			max-height: 400px;
			box-shadow: var(--image-shadow);
			border-radius: 6px;

			img {
				width: 100%;
				height: 100%;
				max-height: 400px;
				object-fit: cover;
			}
		}

		:global(.cover-image img) {
			max-height: 400px;
			object-fit: cover;
		}

		.links {
			display: flex;
			gap: 12px;
			justify-content: center;
		}

		.content {
			display: grid;
			grid-template-columns:
				1fr
				min(var(--main-column-width), 100%)
				1fr;

			:global(> *) {
				grid-column: 2;
			}

			:global(> .full-bleed) {
				grid-column: 1 / 4;
				width: 100%;
				max-width: 1600px;
				margin-left: auto;
				margin-right: auto;
			}
		}

		.tags {
			display: flex;
			align-items: center;
			justify-content: center;
			gap: 5px;
			flex-wrap: wrap;
		}
	}
</style>
