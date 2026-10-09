import { sveltekit } from '@sveltejs/kit/vite';
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import { mdsvex } from 'mdsvex';
import rehypeExternalLinks from 'rehype-external-links';
import rehypeSlug from 'rehype-slug';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';
import path from 'path';

// mdsvex types its plugin lists against unified v9-era Plugin/Settings
// generics so we gotta re-cast them to unknown first to avoid type errors.
const rehypePlugins = /** @type {import('mdsvex').MdsvexOptions['rehypePlugins']} */ (
	/** @type {unknown} */ ([
		rehypeExternalLinks,
		rehypeSlug,
		[
			rehypeAutolinkHeadings,
			{
				behavior: 'prepend',
				properties: { className: ['heading-link'], title: 'Permalink', ariaHidden: 'true' },
				content: {
					type: 'element',
					tagName: 'span',
					properties: {},
					children: [{ type: 'text', value: '#' }]
				}
			}
		]
	])
);

/** @type {import('vite').UserConfig} */
const config = {
	plugins: [
		sveltekit({
			adapter: adapter(),
			alias: {
				$lib: 'src/lib'
			},
			prerender: {
				handleHttpError: 'warn'
			},
			preprocess: [
				vitePreprocess(),
				mdsvex({
					extensions: ['.md'],
					rehypePlugins
				})
			],
			extensions: ['.svelte', '.md']
		})
	],
	resolve: {
		alias: {
			$routes: path.resolve('./src/routes')
		}
	},
	server: {
		allowedHosts: true
	}
};

export default config;
