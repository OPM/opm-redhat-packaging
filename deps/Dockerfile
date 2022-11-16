FROM centos:7 AS stage1
WORKDIR /tmp/opm
ADD . .
RUN echo "Configuring build environment"
RUN /bin/bash /tmp/opm/scripts/setup_buildenv.sh
RUN echo "Making orig sources"
RUN /bin/bash /tmp/opm/scripts/make_sources.sh /tmp/opm/rpmbuild
RUN echo "Making SRPMS"
RUN /bin/bash /tmp/opm/scripts/make_srpms.sh /tmp/opm/rpmbuild
RUN echo "Building RPMS"
RUN /bin/bash /tmp/opm/scripts/make_rpms.sh
FROM scratch as export_stage
COPY --from=stage1 /tmp/opm/rpmbuild .
